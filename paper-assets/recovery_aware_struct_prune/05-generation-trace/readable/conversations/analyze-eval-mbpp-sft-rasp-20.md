# analyze eval mbpp sft rasp 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650.jsonl`
- **Structured JSON:** [`b144d81fba170dccd116.json`](../../sessions/b1/b144d81fba170dccd116.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-19T21:08:18.838037+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T21:08:18.838390+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T21:08:18.838579+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T21:08:18.838718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T21:08:18.838973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 04:00:16,351 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\\n2026-05-20 04:00:16,950 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-20 04:01:40,816 [INFO] Loading MBPP dataset (sanitized, 374 tasks)...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/mbpp.py\\n2026-05-20 04:03:01,101 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/mbpp.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-20 04:03:01,102 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since mbpp couldn't be found on the Hugging Face Hub\\n2026-05-20 04:03:02,105 [WARNING] Using the latest cached version of the dataset since mbpp couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'full' at /root/.cache/huggingface/datasets/mbpp/full/0.0.0/4bb6404fdc6cacfda99d4ac4205087b89d32030c (last modified on Tue May 19 21:26:42 2026).\\n2026-05-20 04:03:02,106 [WARNING] Found the latest cached dataset configuration 'full' at /root/.cache/huggingface/datasets/mbpp/full/0.0.0/4bb6404fdc6cacfda99d4ac4205087b89d32030c (last modified on Tue May 19 21:26:42 2026).\\n2026-05-20 04:03:02,125 [INFO] Loaded 374 problems\\n\\rMBPP:   0%|          | 0/374 [00:00<?, ?it/s]\\rMBPP:   0%|          | 1/374 [00:03<19:33,  3.15s/it]\\rMBPP:   1%|          | 2/374 [00:11<37:21,  6.03s/it]\\rMBPP:   1%|          | 3/374 [00:36<1:31:37, 14.82s/it]\\rMBPP:   1%|          | 4/374 [00:38<1:00:15,  9.77s/it]\\rMBPP:   1%|▏         | 5/374 [00:40<43:54,  7.14s/it]  \\rMBPP:   2%|▏         | 6/374 [01:06<1:21:33, 13.30s/it]\\rMBPP:   2%|▏         | 7/374 [01:09<1:00:21,  9.87s/it]\\rMBPP:   2%|▏         | 8/374 [01:3
…[truncated 6456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T21:08:18.839372+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\\\",\\n  \\\"benchmark\\\": \\\"MBPP\\\",\\n  \\\"pass_at_1\\\": 0.11764705882352941,\\n  \\\"stderr\\\": 0.016660034824618256,\\n  \\\"n_correct\\\": 44,\\n  \\\"n_total\\\": 374,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 810.7433155080214,\\n    \\\"median_response_length\\\": 247.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": 601,\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpm45eq2n5.py\\\\\\\", line 1\\\\n    To solve this problem, I need to find the longest chain of pairs that can be formed from the given set of pairs. Each pair consists of two numbers, and the chain can only be formed if the second number of one pair matches the first number of another pair.\\\\n       ^^^^^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 211\\n    },\\n    {\\n      \\\"task_id\\\": 602,\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpy8xv7j8j.py\\\\\\\", line 3\\\\n    First, I'll create a function called first_repeated_char that takes a string argument.\\\\n            ^\\\\nSyntaxError: unterminated string literal (detected at line 3)\\\\n\\\",\\n      \\\"response_length\\\": 642\\n    },\\n    {\\n      \\\"task_id\\\": 603,\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpl1d972rb.py\\\\\\\", line 3\\\\n    First, I'll create a function to check if a number is lucid. This function will take a number and return true if it is lucid and less than or equal to n, or false otherwise.\\\\n            ^\\\\nSyntaxError: unterminated string literal (detected at line 3)\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": 604,\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"Traceback (most recent call last):\\\\n  File \\\\\\
…[truncated 7701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T21:08:18.839573+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval_mbpp_sft_cka_only_20'}",
  "project": "recovery_aware_struct_prune",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval_mbpp_sft_cka_only_20'}",
    "project": "recovery_aware_struct_prune",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T21:08:18.839718+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval_mbpp_sft_rasp_20'}",
  "project": "recovery_aware_struct_prune",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval_mbpp_sft_rasp_20'}",
    "project": "recovery_aware_struct_prune",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T21:08:18.839850+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6294}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T21:08:18.839975+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6153}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T21:08:18.840136+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "recovery_aware_struct_prune",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "recovery_aware_struct_prune",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T21:08:18.840370+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_mbpp_grpo_standard_20_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_mbpp_sft_standard_20\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_mbpp_grpo_standard_20\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_mbpp_sft_cka_only_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_humaneval_grpo_rasp_20_1p5b_2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_mbpp_grpo_cka_only_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"grpo_shortgpt_20\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sft_shortgpt_20\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"status\": \"DONE\", \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}, \"conclusion\": \"success\"}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"status\": \"DONE\", \"conclusion\": \"s
…[truncated 2287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T21:08:18.840582+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_mbpp_sft_rasp_20",
  "field": "status",
  "value": "DONE",
  "project": "recovery_aware_struct_prune",
  "spec": "{'command': 'python eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'server': 'westd-29022', 'data_path': 'mbpp (sanitized)', 'data_count': 374, 'model_name': 'Qwen2.5-Coder-1.5B RASP 20% + SFT', 'seed': 42, 'checkpoint_source': 'sft_rasp_20', 'eval_data': 'MBPP sanitized 374 tasks', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_mbpp_sft_rasp_20",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune",
    "spec": "{'command': 'python eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'server': 'westd-29022', 'data_path': 'mbpp (sanitized)', 'data_count': 374, 'model_name': 'Qwen2.5-Coder-1.5B RASP 20% + SFT', 'seed': 42, 'checkpoint_source': 'sft_rasp_20', 'eval_data': 'MBPP sanitized 374 tasks', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log'}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T21:08:18.840733+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.6153}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T21:08:18.840859+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_mbpp_sft_rasp_20",
  "field": "hypothesis",
  "value": "SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_mbpp_sft_rasp_20",
    "field": "hypothesis",
    "value": "SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T21:08:18.841049+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_rasp_20\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:07:45.827Z\", \"hypothesis\": \"SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T18:19:54.269Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"code_commit\": \"39afb8c6309aad601973b2b3cd6b4f1a8a3b0b6c\", \"finished_at\": \"2026-05-19T21:05:26.016Z\", \"training_hours\": 2.76}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T18:21:31.440Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:21:37.020361+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:05:32.937237+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\"}}, \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new
…[truncated 572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T21:08:18.841201+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_mbpp_sft_rasp_20",
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
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_mbpp_sft_rasp_20",
    "field": "conclusion",
    "value": "success",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T21:08:18.841407+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_rasp_20\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:07:49.594Z\", \"hypothesis\": \"SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T18:19:54.269Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"code_commit\": \"39afb8c6309aad601973b2b3cd6b4f1a8a3b0b6c\", \"finished_at\": \"2026-05-19T21:05:26.016Z\", \"training_hours\": 2.76}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T18:21:31.440Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:21:37.020361+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:05:32.937237+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\"}}, \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T21:08:18.841573+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_mbpp_sft_rasp_20",
  "field": "metrics",
  "value": "{'pass_at_1': 0.1176, 'stderr': 0.0167, 'n_correct': 44, 'n_total': 374, 'dense_baseline_pass_at_1': 0.5348, 'degradation_pct': 78.01, 'avg_response_length': 810.7, 'median_response_length': 247}",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_mbpp_sft_rasp_20",
    "field": "metrics",
    "value": "{'pass_at_1': 0.1176, 'stderr': 0.0167, 'n_correct': 44, 'n_total': 374, 'dense_baseline_pass_at_1': 0.5348, 'degradation_pct': 78.01, 'avg_response_length': 810.7, 'median_response_length': 247}",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T21:08:18.841744+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_mbpp_sft_rasp_20",
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
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_mbpp_sft_rasp_20",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T21:08:18.841943+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_rasp_20\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:07:55.304Z\", \"hypothesis\": \"SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T18:19:54.269Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"code_commit\": \"39afb8c6309aad601973b2b3cd6b4f1a8a3b0b6c\", \"finished_at\": \"2026-05-19T21:05:26.016Z\", \"training_hours\": 2.76}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T18:21:31.440Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:21:37.020361+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:05:32.937237+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\"}}, \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T21:08:18.842106+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.6207}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T21:08:18.842235+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_mbpp_sft_rasp_20",
  "field": "status",
  "value": "DONE",
  "project": "recovery_aware_struct_prune",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_mbpp_sft_rasp_20",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd', 'log_path': '~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log'}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T21:08:18.842475+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_rasp_20\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:08:00.610Z\", \"hypothesis\": \"SFT RASP 20% model retains more MBPP code generation capability than CKA-only pruning due to recovery-aware pruning preserving structurally important parameters\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T18:19:54.269Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"code_commit\": \"39afb8c6309aad601973b2b3cd6b4f1a8a3b0b6c\", \"finished_at\": \"2026-05-19T21:05:26.016Z\", \"training_hours\": 2.76}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T18:21:31.440Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:21:37.020361+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:05:32.937237+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\"}}, \"notes\": \"Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_toke
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T21:08:18.842705+00:00_

Registry 已更新。以下是分析总结：

## eval_mbpp_sft_rasp_20 结果

| 模型 | pass@1 | n_correct/n_total | 与 Dense 保留率 |
|------|--------|-------------------|----------------|
| **Dense baseline** | 53.48% | 200/374 | 100% |
| **SFT CKA-only 20%** | 12.83% | 48/374 | 24.0% |
| **SFT RASP 20%** | **11.76%** | **44/374** | **22.0%** |
| GRPO CKA-only 20% | 14.17% | 53/374 | 26.5% |

**关键发现：**

1. **pass@1 = 11.76%** (44/374)，比 CKA-only SFT 的 12.83% 低 1.07pp，差 4 题。在 stderr 范围内（±1.7pp），差异不显著。

2. **RASP 在 MBPP 上未能超越 CKA-only**，与 hypothesis 相反。两者都仅保留 dense 的 ~22-24% 能力，说明 80% 结构剪枝对代码生成造成了近乎毁灭性的损伤，SFT 恢复极其有限。

3. **错误模式**：大量样本输出自然语言解释（"To solve this problem..."）而非代码，导致 SyntaxError。median_response_length 仅 247 tokens（CKA-only 为 363），说明 RASP 模型更倾向于短、非代码输出。

4. **对 C2 capability breadth claim 的意义**：MBPP 维度上 RASP 和 CKA-only 表现几乎等价（均极差），不支持 "RASP 在 code 维度优于 CKA-only" 的论点。C2 的 breadth argument 需要依赖其他维度（如 GSM8K，RASP GRPO 60.88% vs CKA-only GRPO 64.22%）或 HumanEval（RASP SFT 10.37% vs CKA-only SFT 0.61%，这个差异显著）来支撑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650"
}
```

</details>

---
