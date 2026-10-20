# ops humaneval registry audit and harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 159
- **Recorded user turns:** 0
- **Tool calls:** 79
- **Original source:** `logs/chats/worker_ops_humaneval_registry_audit_and_harvest_20260519T051210.jsonl`
- **Structured JSON:** [`68a807f1d30764cf9512.json`](../../sessions/68/68a807f1d30764cf9512.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

159 recorded events

### Tool call

_source line 1 · 2026-05-19T05:16:37.635443+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T05:16:37.635933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T05:16:37.636203+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/results/ -name \"*humaneval*\" -o -name \"*human_eval*\" -o -name \"*HumanEval*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/results/ -name \"*humaneval*\" -o -name \"*human_eval*\" -o -name \"*HumanEval*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T05:16:37.636473+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048.log\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json\\n/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T05:16:37.636700+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T05:16:37.637603+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"grpo_unstructured_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:09:44.591Z\", \"updated_at\": \"2026-05-19T04:43:26.240Z\", \"hypothesis\": \"GRPO training on 20% unstructured magnitude-pruned model (no SFT) will show different recovery dynamics than structured pruning methods. Addresses Reviewer W2 concern: why not compare with unstructured pruning? Unstructured pruned model starts at 87.87% GSM8K (higher than structured due to preserved layer dimensions).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/grpo_train.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20 --num_train_steps 100 --seed 42\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"860053\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"pruned_unstructured_20\", \"seed\": 42, \"wandb_run_id\": \"xj46p92t\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_unstructured_20.log\", \"note\": \"Training completed 100/100 steps. Model weights saved successfully. Optimizer state save crashed due to disk full (250G/250G 100%) but model.safetensors is intact.\"}, \"metrics\": {\"reward_mean\": 0.883, \"reward_std\": 0.385, \"loss\": 0.092, \"kl\": 0.34, \"runtime_min\": 47, \"steps\": 100, \"note\": \"reward 2.5x-14x higher than all structured methods. Disk full prevented optimizer state save but model weights intact.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T04:42:17.142Z\"}, \"eval_gsm8k_grpo_cka_only_20_extended_300\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:03:54.973Z\", \"up
…[truncated 38534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T05:16:37.637902+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,etime,command",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ps aux --no-headers -o pid,user,%cpu,%mem,etime,command",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T05:16:37.638062+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T05:16:37.638231+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T05:16:37.638427+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T05:16:37.638762+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.45121951219512196,\\n  \\\"stderr\\\": 0.03885718566889293,\\n  \\\"n_correct\\\": 74,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1771.0182926829268,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 1899\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpmv7f13jp.py\\\\\\\", line 18\\\\n    Once I have the cleaned string, I need to identify each separate group of parentheses. Each group is a balanced set of parentheses that isn't nested within another group. So, how can I find these groups?\\\\n                                                                                                                                               ^\\\\nSyntaxError: unterminated string literal (detected at line 18)\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 865\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/3\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 1207\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/4\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 1501\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/5\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 1527\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/6\\\",\\n    
…[truncated 8056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T05:16:37.638939+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T05:16:37.639212+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.018292682926829267,\\n  \\\"stderr\\\": 0.010464242446963267,\\n  \\\"n_correct\\\": 3,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 512.0,\\n    \\\"median_response_length\\\": 512.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp_93u4b83.py\\\\\\\", line 5\\\\n    In the second example, [1.0, 2.8, 3.0, 4.0, 5.0, 2.0] with a threshold of 0.3, it returns True. Looking at the numbers, 2.8 and 2.0 are 0.8 apart, but wait, maybe there's a closer pair. Oh wait, 2.0 and 2.8 are 0.8 apart, but maybe 2.8 and 3.0 are 0.2 apart, which is less than 0.3. So that's why it's True.\\\\n                                                                                                                                                       \\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmppzo5s965.py\\\\\\\", line 18\\\\n    Once I have the cleaned string, I need to identify each separate group of parentheses. Each group is a balanced set of parentheses that isn't nested within another group. So, how can I find these groups?\\\\n                                                                                                                                               ^\\\\nSyntaxError: unterminated string literal (detected at line 18)\\\\n\\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpxw40s9wq.py\\\\\\\", line 1\\\\n    Okay, I need to write a Python funct
…[truncated 7275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T05:16:37.639420+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T05:16:37.639695+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.03048780487804878,\\n  \\\"stderr\\\": 0.013425108127776123,\\n  \\\"n_correct\\\": 5,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 505.4390243902439,\\n    \\\"median_response_length\\\": 512.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpvz48j0nx.py\\\\\\\", line 1\\\\n    Okay, I need to write a Python function called has_close_elements that checks if any two numbers in a list are within a given threshold. The function takes a list of floats and a float threshold as arguments and returns a boolean. The examples show that when the threshold is 0.5, the first example returns false because 1.0, 2.0, 3.0 are all 1 apart, which is more than 0.5. The second example returns true because 2.0 and 2.8 are 0.8 apart, but wait, that's\\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpc_hzuh80.py\\\\\\\", line 1\\\\n    Okay, I need to solve this problem where I have a string of parentheses and I have to separate the groups into individual strings. The function is named separate_paren_groups and it returns a list of strings. The example given is that the input '( ) (( )) (( ( ))' becomes ['()', '(())', '(()())'].\\\\n            ^^^^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp3h0z6y1k.py\\\\\\\", line 1\\\\n    -> float: return number - math.floor(number). But the code skeleton doesn't 
…[truncated 7269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T05:16:37.639864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T05:16:37.640005+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T05:16:37.640129+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T05:16:37.640247+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T05:16:37.640561+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.11585365853658537,\\n  \\\"stderr\\\": 0.024991655722128053,\\n  \\\"n_correct\\\": 19,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1850.7134146341464,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp2t426odi.py\\\\\\\", line 8\\\\n    if abs(numbers[i] - numbers[j) < threshold:\\\\n                                 ^\\\\nSyntaxError: closing parenthesis ')' does not match opening parenthesis '['\\\\n\\\",\\n      \\\"response_length\\\": 1967\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp0nfep19w.py\\\\\\\", line 11\\\\n    So, how to approach this? Let's think about the example: the input is '( ) (( )) (( ( ))'. So, the string is split into three groups: the first is ( ), the second is ( ( ) ), and the third is ( ( ) ). But the second and third are nested within each other, so they are not separate. So, the output is the first group, and the second and third groups are not separate because they are nested within each other. But the output shows that the second and third gr\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp7gkyrtd1.py\\\\\\\", line 1\\\\n    Okay, I need to write a Python function called truncate_number that takes a float and returns the decimal part. The example given is that truncate_number(3.5) returns 0.5. So how do I get the decimal part from a number? I remember that the integer part is the 
…[truncated 7365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T05:16:37.640727+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T05:16:37.640863+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T05:16:37.641160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.07317073170731707,\\n  \\\"stderr\\\": 0.020335115568277468,\\n  \\\"n_correct\\\": 12,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 420.4512195121951,\\n    \\\"median_response_length\\\": 512.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpehmfp30j.py\\\\\\\", line 3\\\\n    First, I'll look at the examples given to understand how it should work. The first example is [1.0, 2.0, 3.0] with a threshold of 0.5. The function returns false because none of the pairs are within 0.5 apart. For instance, 1.0 and 2.0 are 1.0 apart, which is more than 0.5. Similarly, 2.0 and 3.0 are 1.0 apart. So no pair is within 0.5, hence the function returns false.\\\\n            ^\\\\nSyntaxError: unterminated string literal (detected at line 3)\\\\n\\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp0zvpaqmi.py\\\\\\\", line 14\\\\n    for i, c in enumerate(p paren_string):\\\\n                          ^^^^^^^^^^^^^^\\\\nSyntaxError: invalid syntax. Perhaps you forgot a comma?\\\\n\\\",\\n      \\\"response_length\\\": 427\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpezrc7hgk.py\\\\\\\", line 11\\\\n    return math Modulo(number - math floor(number), 1)\\\\n                ^^^^^^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 230\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/3\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",
…[truncated 7823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T05:16:37.641528+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.10365853658536585,\\n  \\\"stderr\\\": 0.02380221402623906,\\n  \\\"n_correct\\\": 17,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1253.7439024390244,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpvwgr1wbf.py\\\\\\\", line 4\\\\n    for i in range(len(numbers):\\\\n                               ^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 1273\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpkjxc1vht.py\\\\\\\", line 14\\\\n    for i, c in enumerate(p paren_string):\\\\n                          ^^^^^^^^^^^^^^\\\\nSyntaxError: invalid syntax. Perhaps you forgot a comma?\\\\n\\\",\\n      \\\"response_length\\\": 427\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpjjtpii8m.py\\\\\\\", line 11\\\\n    return math Modulo(number - math floor(number), 1)\\\\n                ^^^^^^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 230\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/3\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 336\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/4\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpski9kmdu.py\\\\\\\", line 13\\\\n    return sum(abs(x - mean for x in numbers) / len(numbers)\\\\n              ^\\\\nSyntaxError: '(' was never closed\\\\n\\\",\\n      \\\"r
…[truncated 7995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T05:16:37.641716+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T05:16:37.641981+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.018292682926829267,\\n  \\\"stderr\\\": 0.010464242446963267,\\n  \\\"n_correct\\\": 3,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 505.890243902439,\\n    \\\"median_response_length\\\": 512.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpbe4m03sy.py\\\\\\\", line 5\\\\n    But how to compare all pairs? One way is to loop through each number in the list, and for each number, compare it to every other number in the list that comes after it. Because if I compare all combinations, I can avoid checking same pairs twice. So for each index i, I compare the number at i to the numbers at j where j > i. This way, I'll check all unique pairs once.\\\\n                                                                                        \\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp6pivfvm9.py\\\\\\\", line 14\\\\n    First, I think about the process of parsing the string. I need to find all the groups of parentheses that are balanced and not nested. So, each group starts with an open parenthesis and ends with a corresponding closed parenthesis, and they don't have any other groups inside them. So, the first thing is to find all the groups that are not nested within each other.\\\\n                                                                                           \\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  Fil
…[truncated 7161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T05:16:37.642393+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.10365853658536585,\\n  \\\"stderr\\\": 0.02380221402623906,\\n  \\\"n_correct\\\": 17,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1843.030487804878,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpkfab9yoh.py\\\\\\\", line 3\\\\n    def has_close_elements(numbers: List[float, threshold: float) -> bool:\\\\n                                                                ^\\\\nSyntaxError: closing parenthesis ')' does not match opening parenthesis '['\\\\n\\\",\\n      \\\"response_length\\\": 1427\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpnu3w4iwo.py\\\\\\\", line 14\\\\n    First, I think about the process of parsing the string. I need to find all the groups of parentheses that are balanced and not nested. So, each group starts with an open parenthesis and ends with a corresponding closed parenthesis, and they don't have any other groups inside them. So, the first thing is to find all the groups that are not nested within each other.\\\\n                                                                                           \\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 936\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/3\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpdaptyekb.py\\\\\\\", line 3\\\\n    Let's think about 
…[truncated 7365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T05:16:37.642586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T05:16:37.642898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.10365853658536585,\\n  \\\"stderr\\\": 0.02380221402623906,\\n  \\\"n_correct\\\": 17,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 417.6280487804878,\\n    \\\"median_response_length\\\": 512.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp7yjkpmy7.py\\\\\\\", line 3\\\\n    First, I'll look at the examples given to understand how it should work. The first example is [1.0, 2.0, 3.0] with a threshold of 0.5. The function returns false because none of the pairs are within 0.5 apart. For instance, 1.0 and 2.0 are 1.0 apart, which is more than 0.5. Similarly, 2.0 and 3.0 are 1.0 apart. So no pair is within 0.5, hence the function returns false.\\\\n            ^\\\\nSyntaxError: unterminated string literal (detected at line 3)\\\\n\\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpat1ripps.py\\\\\\\", line 18\\\\n    \\\\\\\"\\\\\\\"\\\\\\\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\\\\n    ^\\\\nSyntaxError: unterminated triple-quoted string literal (detected at line 79)\\\\n\\\",\\n      \\\"response_length\\\": 512\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"Traceback (most recent call last):\\\\n  File \\\\\\\"/tmp/tmp5wmh60xn.py\\\\\\\", line 18, in &lt;module>\\\\n    check(truncate_number)\\\\n  File \\\\\\\"/tmp/tmp5wmh60xn.py\\\\\\\", line 14, in check\\\\n    assert candidate(3.5) == 0.5\\\\n           ^^^^^^^^^^^^^
…[truncated 7773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T05:16:37.643064+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ps -eo pid,user,pcpu,pmem,etime,args",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ps -eo pid,user,pcpu,pmem,etime,args",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T05:16:37.643399+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.14634146341463414,\\n  \\\"stderr\\\": 0.02759966855362771,\\n  \\\"n_correct\\\": 24,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1168.530487804878,\\n    \\\"median_response_length\\\": 948.5\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpuf1h0ayj.py\\\\\\\", line 3\\\\n    First, I'll look at the examples given to understand how it should work. The first example is [1.0, 2.0, 3.0] with a threshold of 0.5. The function returns false because none of the pairs are within 0.5 apart. For instance, 1.0 and 2.0 are 1.0 apart, which is more than 0.5. Similarly, 2.0 and 3.0 are 1.0 apart. So no pair is within 0.5, hence the function returns false.\\\\n            ^\\\\nSyntaxError: unterminated string literal (detected at line 3)\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpt6j9cm0h.py\\\\\\\", line 18\\\\n    \\\\\\\"\\\\\\\"\\\\\\\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\\\\n    ^\\\\nSyntaxError: unterminated triple-quoted string literal (detected at line 271)\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"Traceback (most recent call last):\\\\n  File \\\\\\\"/tmp/tmp28uimlfy.py\\\\\\\", line 18, in &lt;module>\\\\n    check(truncate_number)\\\\n  File \\\\\\\"/tmp/tmp28uimlfy.py\\\\\\\", line 14, in check\\\\n    assert candidate(3.5) == 0.5\\\\n           ^^^^^^^^^^
…[truncated 7887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T05:16:37.643662+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 11:33:01,724 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\n2026-05-19 11:33:02,357 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-19 11:34:27,562 [INFO] Loading HumanEval dataset...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\n2026-05-19 11:35:47,814 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-19 11:35:47,815 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\n2026-05-19 11:35:48,819 [WARNING] Using the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 11:35:48,820 [WARNING] Found the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 11:35:48,831 [INFO] Loaded 164 problems\\n\\rHumanEval:   0%|          | 0/164 [00:00<?, ?it/s]\\rHumanEval:   1%|          | 1/164 [01:44<4:42:33, 104.01s/it]\\rHumanEval:   1%|          | 2/164 [03:27<4:39:17, 103.44s/it]\\rHumanEval:   2%|▏         | 3/164 [03:31<2:36:12, 58.22s/it] \\rHumanEval:   2%|▏         | 4/164 [03:39<1:42:31, 38.45s/it]\\rHumanE
…[truncated 5911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T05:16:37.643875+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 12:11:30,925 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\n2026-05-19 12:11:31,527 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-19 12:12:54,902 [INFO] Loading HumanEval dataset...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\n2026-05-19 12:13:15,128 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-19 12:13:15,129 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\n2026-05-19 12:13:16,131 [WARNING] Using the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 12:13:16,131 [WARNING] Found the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 12:13:16,150 [INFO] Loaded 164 problems\\n\\rHumanEval:   0%|          | 0/164 [00:00<?, ?it/s]\\rHumanEval:   1%|          | 1/164 [01:43<4:42:06, 103.84s/it]\\rHumanEval:   1%|          | 2/164 [03:26<4:39:04, 103.36s/it]\\rHumanEval:   2%|▏         | 3/164 [03:35<2:41:15, 60.10s/it] \\rHumanEval:   2%|▏         | 4/164 [03:45<1:47:04, 40.15s/it]\\rHuman
…[truncated 4251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T05:16:37.644086+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID USER     %CPU %MEM     ELAPSED COMMAND\\n     1 root      0.0  0.0    16:21:32 bash /init/boot/boot.sh\\n   917 root      2.3  0.0    16:21:29 /bin/supervisord -c /init/supervisor/supervisor.ini\\n   933 root      0.0  0.0    16:21:29 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\n   935 root      0.0  0.0    16:21:29 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\n   938 root      0.1  0.0    16:21:29 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\n   939 root      0.0  0.0    16:21:29 proxy -c /init/proxy/proxy-hot-backup.ini\\n   940 root      0.0  0.0    16:21:29 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\n   941 root      0.1  0.0    16:21:29 proxy -c /init/proxy/proxy.ini\\n  1052 root      0.1  0.0    16:21:29 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_4_ocohnk/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_4_ocohnk/startup_error\\n 15617 root      0.0  0.0    12:45:22 sshd: root@notty\\n 19609 root      0.0  0.0    11:20:20 tmux new-session -d -s math500_standard_grpo_fair source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair_v2.json --max_new_tokens 2048 2>&1 | tee ~/runs/recovery_aware_struct_prune/math500_standard_grpo_fair_v2.log\\n 56146 root      0.0  0.0    03:38:09 bash -c rm -f /tmp/agent-ml-exit/eval_math500_sft_standard_20_2048_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$
…[truncated 6158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T05:16:37.644336+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T05:16:37.644496+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_2048\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:01.505Z\", \"updated_at\": \"2026-05-19T05:14:01.505Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1443}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T05:16:37.644629+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T05:16:37.644762+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_2048\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:03.359Z\", \"updated_at\": \"2026-05-19T05:14:03.359Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1395}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T05:16:37.644886+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T05:16:37.645019+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:00:51.937Z\", \"updated_at\": \"2026-05-19T05:14:04.327Z\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1843, \"median_response_length\": 2048}, \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.169}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T05:16:37.645148+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%."
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T05:16:37.645295+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_2048\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:06.291Z\", \"updated_at\": \"2026-05-19T05:14:06.291Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.134}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T05:16:37.645424+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T05:16:37.645552+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_512\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:07.703Z\", \"updated_at\": \"2026-05-19T05:14:07.703Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1365}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T05:16:37.645671+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T05:16:37.645806+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_512\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:08.589Z\", \"updated_at\": \"2026-05-19T05:14:08.589Z\", \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1484}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T05:16:37.645930+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness."
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T05:16:37.646053+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_512\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:09.530Z\", \"updated_at\": \"2026-05-19T05:14:09.530Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1639}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T05:16:37.646167+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model."
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T05:16:37.646308+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_512\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.526Z\", \"updated_at\": \"2026-05-19T05:14:10.526Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1411}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T05:16:37.646432+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "hypothesis",
  "value": "HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "hypothesis",
    "value": "HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model."
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T05:16:37.646552+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_512\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:11.166Z\", \"updated_at\": \"2026-05-19T05:14:11.167Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1418}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T05:16:37.646702+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json'}"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T05:16:37.646848+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0942}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T05:16:37.646975+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json'}"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T05:16:37.647111+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0825}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T05:16:37.647232+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json', 'note': 'Old stage2 model (v8), not fair v5. Needs re-eval with fair model.'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json', 'note': 'Old stage2 model (v8), not fair v5. Needs re-eval with fair model.'}"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T05:16:37.647393+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0786}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T05:16:37.647525+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json', 'note': 'Old stage2 model (v9), not fair v5. Needs re-eval with fair model.'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164 problems, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json', 'note': 'Old stage2 model (v9), not fair v5. Needs re-eval with fair model.'}"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T05:16:37.647667+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0999}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T05:16:37.647788+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'}"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T05:16:37.647922+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0837}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T05:16:37.648045+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_standard_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_standard_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json'}"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T05:16:37.648184+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0804}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T05:16:37.648328+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json'}"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T05:16:37.648466+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0791}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T05:16:37.648589+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json', 'note': 'Old stage2 model (v8), not fair v5.'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json', 'note': 'Old stage2 model (v8), not fair v5.'}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T05:16:37.648725+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.134}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T05:16:37.648848+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json', 'note': 'Old stage2 model (v9), not fair v5.'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164 problems, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json', 'note': 'Old stage2 model (v9), not fair v5.'}"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T05:16:37.648989+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0798}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T05:16:37.649139+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T05:16:37.649284+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_2048\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:01.505Z\", \"updated_at\": \"2026-05-19T05:14:58.809Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3661}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T05:16:37.649410+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T05:16:37.649534+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_2048\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:03.359Z\", \"updated_at\": \"2026-05-19T05:14:59.181Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2241}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T05:16:37.649652+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T05:16:37.649791+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:00:51.937Z\", \"updated_at\": \"2026-05-19T05:15:00.195Z\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1843, \"median_response_length\": 2048}, \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3324}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T05:16:37.649917+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-19T05:16:37.650089+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_2048\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:06.291Z\", \"updated_at\": \"2026-05-19T05:15:00.741Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2618}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T05:16:37.650498+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T05:16:37.650720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_512\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:07.703Z\", \"updated_at\": \"2026-05-19T05:15:01.558Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2865}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T05:16:37.650911+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-19T05:16:37.651097+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_512\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:08.589Z\", \"updated_at\": \"2026-05-19T05:15:02.100Z\", \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.341}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T05:16:37.651295+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T05:16:37.651501+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_512\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:09.530Z\", \"updated_at\": \"2026-05-19T05:15:03.024Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3595}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-19T05:16:37.651682+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T05:16:37.651869+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_512\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.526Z\", \"updated_at\": \"2026-05-19T05:15:03.489Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3612}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-19T05:16:37.652043+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-19T05:16:37.652222+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_512\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:11.166Z\", \"updated_at\": \"2026-05-19T05:15:04.006Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3287}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-19T05:16:37.652473+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path .../eval_humaneval_unpruned_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path .../eval_humaneval_unpruned_2048.json', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json'}"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-19T05:16:37.652720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:01.505Z\", \"updated_at\": \"2026-05-19T05:15:11.969Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path .../eval_humaneval_unpruned_2048.json\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2752}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-19T05:16:37.652922+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../sft_rasp_20_westd --max_new_tokens 2048', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../sft_rasp_20_westd --max_new_tokens 2048', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json'}"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T05:16:37.653136+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:03.359Z\", \"updated_at\": \"2026-05-19T05:15:14.764Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2374}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-19T05:16:37.653312+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json', 'note': 'Old stage2 v8, not fair v5'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json', 'note': 'Old stage2 v8, not fair v5'}"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-19T05:16:37.653497+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:00:51.937Z\", \"updated_at\": \"2026-05-19T05:15:18.038Z\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1843, \"median_response_length\": 2048}, \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\", \"note\": \"Old stage2 v8, not fair v5\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2407}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-19T05:16:37.653640+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9 --max_new_tokens 2048', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json', 'note': 'Old stage2 v9, not fair v5'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9 --max_new_tokens 2048', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164, max_new_tokens=2048)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json', 'note': 'Old stage2 v9, not fair v5'}"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-19T05:16:37.653810+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:06.291Z\", \"updated_at\": \"2026-05-19T05:15:20.961Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json\", \"note\": \"Old stage2 v9, not fair v5\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2405}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-19T05:16:37.653952+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'DeepSeek-R1-Distill-Qwen-7B (unpruned)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'}"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-19T05:16:37.654103+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:07.703Z\", \"updated_at\": \"2026-05-19T05:15:23.372Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3575}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-19T05:16:37.654233+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../sft_standard_20_westd', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_standard_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../sft_standard_20_westd', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_standard_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json'}"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-19T05:16:37.654432+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:08.589Z\", \"updated_at\": \"2026-05-19T05:15:26.134Z\", \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_standard_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2555}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-19T05:16:37.654572+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../sft_rasp_20_westd', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../sft_rasp_20_westd', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'sft_rasp_20_westd', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json'}"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-19T05:16:37.654723+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:09.530Z\", \"updated_at\": \"2026-05-19T05:15:28.870Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2867}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-19T05:16:37.654854+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json', 'note': 'Old stage2 v8, not fair v5'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_standard_20_v8/checkpoint-50', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json', 'note': 'Old stage2 v8, not fair v5'}"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-19T05:16:37.655010+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.526Z\", \"updated_at\": \"2026-05-19T05:15:30.894Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json\", \"note\": \"Old stage2 v8, not fair v5\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.254}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-19T05:16:37.655144+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json', 'note': 'Old stage2 v9, not fair v5'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9', 'server': 'westd-29022', 'data_path': 'HumanEval', 'data_count': 164, 'model_name': 'grpo_stage2_rasp_20_v9', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'eval_data': 'HumanEval (164, max_new_tokens=512)', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9', 'log_path': '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json', 'note': 'Old stage2 v9, not fair v5'}"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-19T05:16:37.655313+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:11.166Z\", \"updated_at\": \"2026-05-19T05:15:33.276Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json\", \"note\": \"Old stage2 v9, not fair v5\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3245}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-19T05:16:37.655479+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "metrics",
  "value": "{'pass_at_1': 0.4512, 'n_correct': 74, 'n_total': 164, 'max_new_tokens': 2048, 'avg_response_length': 1771, 'median_response_length': 2048}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "metrics",
    "value": "{'pass_at_1': 0.4512, 'n_correct': 74, 'n_total': 164, 'max_new_tokens': 2048, 'avg_response_length': 1771, 'median_response_length': 2048}"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T05:16:37.655635+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:01.505Z\", \"updated_at\": \"2026-05-19T05:15:41.466Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path .../eval_humaneval_unpruned_2048.json\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json\"}, \"metrics\": {\"pass_at_1\": 0.4512, \"n_correct\": 74, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1771, \"median_response_length\": 2048}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1574}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-19T05:16:37.655767+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "metrics",
  "value": "{'pass_at_1': 0.1037, 'n_correct': 17, 'n_total': 164, 'max_new_tokens': 2048, 'avg_response_length': 1253.7, 'median_response_length': 2048}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "metrics",
    "value": "{'pass_at_1': 0.1037, 'n_correct': 17, 'n_total': 164, 'max_new_tokens': 2048, 'avg_response_length': 1253.7, 'median_response_length': 2048}"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-19T05:16:37.655914+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:03.359Z\", \"updated_at\": \"2026-05-19T05:15:42.536Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"n_correct\": 17, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1892}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-19T05:16:37.656050+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "metrics",
  "value": "{'pass_at_1': 0.1463, 'n_correct': 24, 'n_total': 164, 'max_new_tokens': 2048, 'avg_response_length': 1168.5, 'median_response_length': 948.5}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "metrics",
    "value": "{'pass_at_1': 0.1463, 'n_correct': 24, 'n_total': 164, 'max_new_tokens': 2048, 'avg_response_length': 1168.5, 'median_response_length': 948.5}"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-19T05:16:37.656199+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:06.291Z\", \"updated_at\": \"2026-05-19T05:15:43.986Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json\", \"note\": \"Old stage2 v9, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.1463, \"n_correct\": 24, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1168.5, \"median_response_length\": 948.5}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1979}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-19T05:16:37.656352+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "metrics",
  "value": "{'pass_at_1': 0.0183, 'n_correct': 3, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 512, 'median_response_length': 512}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "metrics",
    "value": "{'pass_at_1': 0.0183, 'n_correct': 3, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 512, 'median_response_length': 512}"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-19T05:16:37.656499+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:07.703Z\", \"updated_at\": \"2026-05-19T05:15:45.222Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"n_correct\": 3, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 512, \"median_response_length\": 512}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1559}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-19T05:16:37.656635+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "metrics",
  "value": "{'pass_at_1': 0.0305, 'n_correct': 5, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 505.4, 'median_response_length': 512}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "metrics",
    "value": "{'pass_at_1': 0.0305, 'n_correct': 5, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 505.4, 'median_response_length': 512}"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-19T05:16:37.656783+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:08.589Z\", \"updated_at\": \"2026-05-19T05:15:46.651Z\", \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_standard_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.0305, \"n_correct\": 5, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 505.4, \"median_response_length\": 512}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1617}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-19T05:16:37.656912+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "metrics",
  "value": "{'pass_at_1': 0.0732, 'n_correct': 12, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 420.5, 'median_response_length': 512}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "metrics",
    "value": "{'pass_at_1': 0.0732, 'n_correct': 12, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 420.5, 'median_response_length': 512}"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-19T05:16:37.657061+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:09.530Z\", \"updated_at\": \"2026-05-19T05:15:47.543Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\"}, \"metrics\": {\"pass_at_1\": 0.0732, \"n_correct\": 12, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 420.5, \"median_response_length\": 512}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1632}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-19T05:16:37.657197+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "metrics",
  "value": "{'pass_at_1': 0.0183, 'n_correct': 3, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 505.9, 'median_response_length': 512}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "metrics",
    "value": "{'pass_at_1': 0.0183, 'n_correct': 3, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 505.9, 'median_response_length': 512}"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-19T05:16:37.657370+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.526Z\", \"updated_at\": \"2026-05-19T05:15:48.959Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json\", \"note\": \"Old stage2 v8, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"n_correct\": 3, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 505.9, \"median_response_length\": 512}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1526}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-19T05:16:37.657505+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "metrics",
  "value": "{'pass_at_1': 0.1037, 'n_correct': 17, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 417.6, 'median_response_length': 512}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "metrics",
    "value": "{'pass_at_1': 0.1037, 'n_correct': 17, 'n_total': 164, 'max_new_tokens': 512, 'avg_response_length': 417.6, 'median_response_length': 512}"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-19T05:16:37.657654+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:11.166Z\", \"updated_at\": \"2026-05-19T05:15:50.117Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json\", \"note\": \"Old stage2 v9, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"n_correct\": 17, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 417.6, \"median_response_length\": 512}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1691}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-19T05:16:37.657834+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-19T05:16:37.657981+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:01.505Z\", \"updated_at\": \"2026-05-19T05:15:55.654Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path .../eval_humaneval_unpruned_2048.json\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json\"}, \"metrics\": {\"pass_at_1\": 0.4512, \"n_correct\": 74, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1771, \"median_response_length\": 2048}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1607}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-19T05:16:37.658109+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-19T05:16:37.658248+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:03.359Z\", \"updated_at\": \"2026-05-19T05:15:56.595Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"n_correct\": 17, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-19T05:16:37.658405+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-19T05:16:37.658549+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:00:51.937Z\", \"updated_at\": \"2026-05-19T05:15:57.104Z\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1843, \"median_response_length\": 2048}, \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\", \"note\": \"Old stage2 v8, not fair v5\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1803}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-19T05:16:37.658678+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-19T05:16:37.658816+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:06.291Z\", \"updated_at\": \"2026-05-19T05:15:58.142Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json\", \"note\": \"Old stage2 v9, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.1463, \"n_correct\": 24, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1168.5, \"median_response_length\": 948.5}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3949}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-19T05:16:37.658949+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-19T05:16:37.659088+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:07.703Z\", \"updated_at\": \"2026-05-19T05:15:58.586Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"n_correct\": 3, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 512, \"median_response_length\": 512}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3005}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-19T05:16:37.659214+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-19T05:16:37.659354+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-19T05:16:37.659493+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:08.589Z\", \"updated_at\": \"2026-05-19T05:15:59.680Z\", \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_standard_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.0305, \"n_correct\": 5, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 505.4, \"median_response_length\": 512}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.503}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-19T05:16:37.659644+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:09.530Z\", \"updated_at\": \"2026-05-19T05:16:00.182Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\"}, \"metrics\": {\"pass_at_1\": 0.0732, \"n_correct\": 12, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 420.5, \"median_response_length\": 512}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4184}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-19T05:16:37.659772+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-19T05:16:37.659911+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.526Z\", \"updated_at\": \"2026-05-19T05:16:00.873Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json\", \"note\": \"Old stage2 v8, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"n_correct\": 3, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 505.9, \"median_response_length\": 512}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1936}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-19T05:16:37.660043+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-19T05:16:37.660181+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_512\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:11.166Z\", \"updated_at\": \"2026-05-19T05:16:01.073Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json\", \"note\": \"Old stage2 v9, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"n_correct\": 17, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 417.6, \"median_response_length\": 512}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.186}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-19T05:16:37.660346+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_2048",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_2048",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-19T05:16:37.660512+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:01.505Z\", \"updated_at\": \"2026-05-19T05:16:05.609Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model (DeepSeek-R1-Distill-Qwen-7B) with max_new_tokens=2048. Upper bound baseline for all pruned model HumanEval comparisons.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path .../eval_humaneval_unpruned_2048.json\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned_2048.json\"}, \"metrics\": {\"pass_at_1\": 0.4512, \"n_correct\": 74, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1771, \"median_response_length\": 2048}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:05.609Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3586}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-19T05:16:37.660663+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_2048",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_2048",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-19T05:16:37.660824+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:03.359Z\", \"updated_at\": \"2026-05-19T05:16:06.494Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=2048. Compares SFT RASP vs SFT Standard (11.59%) code generation capability post-pruning.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_2048.json\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"n_correct\": 17, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:06.494Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2627}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-19T05:16:37.660965+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-19T05:16:37.661124+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:00:51.937Z\", \"updated_at\": \"2026-05-19T05:16:06.976Z\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1843, \"median_response_length\": 2048}, \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. Old stage2 model (v8 checkpoint-50), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\", \"note\": \"Old stage2 v8, not fair v5\"}, \"completed_at\": \"2026-05-19T05:16:06.976Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2705}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-19T05:16:37.661287+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_2048",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_2048",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-19T05:16:37.661459+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:06.291Z\", \"updated_at\": \"2026-05-19T05:16:07.931Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=2048. Old stage2 model (v9), not fair v5, needs re-eval with fair model. Highest pruned HumanEval score at 14.63%.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json\", \"note\": \"Old stage2 v9, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.1463, \"n_correct\": 24, \"n_total\": 164, \"max_new_tokens\": 2048, \"avg_response_length\": 1168.5, \"median_response_length\": 948.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:07.931Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2894}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-19T05:16:37.661601+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_unpruned_512",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_unpruned_512",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-19T05:16:37.661778+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_unpruned_512\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:07.703Z\", \"updated_at\": \"2026-05-19T05:16:08.388Z\", \"hypothesis\": \"HumanEval pass@1 for unpruned Dense model with max_new_tokens=512. Token budget too short for code generation; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"n_correct\": 3, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 512, \"median_response_length\": 512}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:08.388Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2908}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-19T05:16:37.661924+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_512",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_512",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-19T05:16:37.662083+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_512\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:08.589Z\", \"updated_at\": \"2026-05-19T05:16:09.481Z\", \"hypothesis\": \"HumanEval pass@1 for SFT Standard 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_standard_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.0305, \"n_correct\": 5, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 505.4, \"median_response_length\": 512}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:09.481Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3955}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-19T05:16:37.662227+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_rasp_20_512",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_rasp_20_512",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-19T05:16:37.662412+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_rasp_20_512\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:09.530Z\", \"updated_at\": \"2026-05-19T05:16:09.788Z\", \"hypothesis\": \"HumanEval pass@1 for SFT RASP 20% with max_new_tokens=512. Token budget too short; included for completeness.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../sft_rasp_20_westd\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\"}, \"metrics\": {\"pass_at_1\": 0.0732, \"n_correct\": 12, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 420.5, \"median_response_length\": 512}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:09.788Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2646}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-19T05:16:37.662552+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_512",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_512",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-19T05:16:37.662677+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_rasp_20_512",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_rasp_20_512",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-19T05:16:37.662834+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_512\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.526Z\", \"updated_at\": \"2026-05-19T05:16:11.014Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=512. Old stage2 model (v8), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_standard_20_v8/checkpoint-50\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20.json\", \"note\": \"Old stage2 v8, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"n_correct\": 3, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 505.9, \"median_response_length\": 512}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:11.014Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3057}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-19T05:16:37.663014+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_rasp_20_512\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:11.166Z\", \"updated_at\": \"2026-05-19T05:16:11.298Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO RASP 20% with max_new_tokens=512. Old stage2 model (v9), not fair v5, needs re-eval with fair model.\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path .../grpo_stage2_rasp_20_v9\", \"server\": \"westd-29022\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"eval_data\": \"HumanEval (164, max_new_tokens=512)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20.json\", \"note\": \"Old stage2 v9, not fair v5\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"n_correct\": 17, \"n_total\": 164, \"max_new_tokens\": 512, \"avg_response_length\": 417.6, \"median_response_length\": 512}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:16:11.298Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.265}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 159 · 2026-05-19T05:16:37.663224+00:00_

9 个条目全部注册完成。

---

## HumanEval 结果清单

### @2048 tokens（主要结果）

| Registry ID | Model | pass@1 | n_correct/164 | Fair v5? |
|---|---|---|---|---|
| `eval_humaneval_unpruned_2048` | Dense | **45.12%** | 74 | N/A |
| `eval_humaneval_sft_standard_20_2048_v2` | SFT Standard 20% | 11.59% | 19 | N/A (SFT) |
| `eval_humaneval_sft_rasp_20_2048` | SFT RASP 20% | 10.37% | 17 | N/A (SFT) |
| `eval_humaneval_grpo_standard_20_2048` | GRPO Standard 20% (v8) | 10.37% | 17 | **No** (old stage2) |
| `eval_humaneval_grpo_rasp_20_2048` | GRPO RASP 20% (v9) | **14.63%** | 24 | **No** (old stage2) |

### @512 tokens（token 不足，仅供参考）

| Registry ID | Model | pass@1 | n_correct/164 |
|---|---|---|---|
| `eval_humaneval_unpruned_512` | Dense | 1.83% | 3 |
| `eval_humaneval_sft_standard_20_512` | SFT Standard 20% | 3.05% | 5 |
| `eval_humaneval_sft_rasp_20_512` | SFT RASP 20% | 7.32% | 12 |
| `eval_humaneval_grpo_standard_20_512` | GRPO Standard 20% (v8) | 1.83% | 3 |
| `eval_humaneval_grpo_rasp_20_512` | GRPO RASP 20% (v9) | 10.37% | 17 |

### 运行中

| Eval | GPU | PID | Progress | 当前 pass@1 | 预计剩余 |
|---|---|---|---|---|---|
| SFT CKA-only @2048 | cuda:2 | 63783 | 90/164 (55%) | **0.00%** | ~1.5h |
| GRPO CKA-only @2048 | cuda:1 | 66531 | 66/164 (40%) | **~33%** | ~1.5h |

### 关键发现
- SFT CKA-only HumanEval 到 90/164 仍然 pass@1=0.00%，代码生成能力完全丧失
- GRPO CKA-only 约 33% pass@1，远高于其他剪枝模型（10-15%），接近 Dense 的 45%
- GRPO RASP (v9) 在所有已完成剪枝模型中 HumanEval 最高（14.63%），但这是旧 stage2 模型
- 所有 GRPO 条目（Standard/RASP）均为旧 stage2，已标注 "needs re-eval with fair model"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_humaneval_registry_audit_and_harvest_20260519T051210"
}
```

</details>

---
