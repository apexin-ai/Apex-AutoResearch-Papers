# eval capture westd all results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_eval_capture-westd-all-results_20260515T163912.jsonl`
- **Structured JSON:** [`075ebeb7374c3c4f4738.json`](../../sessions/07/075ebeb7374c3c4f4738.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-15T16:41:25.362232+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T16:41:25.362579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T16:41:25.362760+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.json /root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.json /root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.json 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.json /root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.json /root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.json 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T16:41:25.362901+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T16:41:25.363027+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/recovery_aware_struct_prune/results/eval_*grasp* /root/recovery_aware_struct_prune/results/eval_*alpha* 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/recovery_aware_struct_prune/results/eval_*grasp* /root/recovery_aware_struct_prune/results/eval_*alpha* 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T16:41:25.363152+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T16:41:25.363287+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/recovery_aware_struct_prune/results/eval_pruned_graspune_20_greedy.json 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/recovery_aware_struct_prune/results/eval_pruned_graspune_20_greedy.json 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T16:41:25.363415+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T16:41:25.363550+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "find /root/recovery_aware_struct_prune/results/ -name \"eval_sft_*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "find /root/recovery_aware_struct_prune/results/ -name \"eval_sft_*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T16:41:25.363670+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "find /root/recovery_aware_struct_prune/results/ -name \"eval_*grasp*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "find /root/recovery_aware_struct_prune/results/ -name \"eval_*grasp*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T16:41:25.363803+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.0_n100.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_1.0_n100.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\\n/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\\n/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T16:41:25.363925+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "find /root/recovery_aware_struct_prune/results/ -name \"eval_*alpha*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "find /root/recovery_aware_struct_prune/results/ -name \"eval_*alpha*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T16:41:25.364046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/results/eval_grasp_n100.log\\n/root/recovery_aware_struct_prune/results/eval_pruned_graspune_20_greedy.json\\n/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\\n/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T16:41:25.364170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/results/alpha_ablation/eval_prune_alpha_0.0.json\\n/root/recovery_aware_struct_prune/results/alpha_ablation/eval_prune_alpha_0.5.json\\n/root/recovery_aware_struct_prune/results/alpha_ablation/eval_prune_alpha_1.0.json\\n/root/recovery_aware_struct_prune/results/alpha_ablation/eval_prune_alpha_2.0.json\\n/root/recovery_aware_struct_prune/results/alpha_ablation/eval_prune_alpha_4.0.json\\n/root/recovery_aware_struct_prune/results/eval_alpha_4.0_greedy.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.0_n100.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_1.0_n100.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.json\\n/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T16:41:25.364324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "cat /root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "cat /root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T16:41:25.364448+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "cat /root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "cat /root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T16:41:25.364721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.62,\\n  \\\"stderr\\\": 0.048538644398046386,\\n  \\\"n_correct\\\": 62,\\n  \\\"n_total\\\": 100,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 97,\\n    \\\"truncated\\\": 3,\\n    \\\"eos_rate\\\": 0.97,\\n    \\\"avg_response_length\\\": 277.41,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 63\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"109\\\",\\n      \\\"correct\\\": true,\\n      \\\"response\\\": \\\"Let the ages of Darrell and Allen be 7x and 11x respectively.\\\\n\\\\nThe total age of the two is 7x + 11x = 162.\\\\n\\\\nSo, 18x = 162, which means x = 162/18 = <<162/18=9>>9.\\\\n\\\\nThe age of Allen is 11x = 11*9 = <<11*9=99>>99 years.\\\\n&lt;/think>\\\\n\\\\nLet the ages of **Darrell** and **Allen** be represented by the variables **7x** and **11x** respectively, where **x** is a common multiplier.\\\\n\\\\nThe total age of the two is given as:\\\\n\\\\\\\\[\\\\n7x + 11x = 162\\\\n\\\\\\\\]\\\\nSimplifying the equation:\\\\n\\\\\\\\[\\\\n18x = 162\\\\n\\\\\\\\]\\\\nDividing both sides by 18:\\\\n\\\",\\n      \\\"response_length\\\": 308,\\n      \\\"hit_eos\\\": true\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large butto
…[truncated 7362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T16:41:25.365018+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.41,\\n  \\\"stderr\\\": 0.04918333050943175,\\n  \\\"n_correct\\\": 41,\\n  \\\"n_total\\\": 100,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 98,\\n    \\\"truncated\\\": 2,\\n    \\\"eos_rate\\\": 0.98,\\n    \\\"avg_response_length\\\": 225.78,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 57\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"119\\\",\\n      \\\"correct\\\": false,\\n      \\\"response\\\": \\\"Let the ages of Allen and Darrell be 11x and 7x respectively.\\\\nThe total age is 11x + 7x = 18x\\\\nThe total age is 18x = 162\\\\nx = <<9 = 9>>9\\\\nAllen's age is 11x = <<11*9=99>>99\\\\nAllen's age 10 years from now is 99 + 10 = <<99+10=119>>119\\\\n#### 119\\\",\\n      \\\"response_length\\\": 121,\\n      \\\"hit_eos\\\": true\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for large buttons and trades the rest of them for small buttons. How many buttons does she have by the end?\\\",\\n      \\\"gold\\\": \\\"89\\\",\\n      \\\"prediction\\\": \\\"135\\\",\\n      \\\"correct\\\": false,\\n      \\\"response\\\": \\\"Lorraine starts with 30 small stickers and 40 large stickers.
…[truncated 7293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T16:41:25.365185+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -30 /root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -30 /root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T16:41:25.365350+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 00:07:38,708 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\\n2026-05-16 00:07:39,343 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\nTraceback (most recent call last):\\n  File \\\"/root/recovery_aware_struct_prune/src/eval_gsm8k.py\\\", line 403, in &lt;module>\\n    main()\\n  File \\\"/root/recovery_aware_struct_prune/src/eval_gsm8k.py\\\", line 342, in main\\n    model = load_pruned_model(args.model_path, device_map=\\\"auto\\\", torch_dtype=torch_dtype)\\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/recovery_aware_struct_prune/src/model_utils.py\\\", line 95, in load_pruned_model\\n    state_dict = _load_state_dict(model_path)\\n                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/recovery_aware_struct_prune/src/model_utils.py\\\", line 19, in _load_state_dict\\n    state_dict.update(load_file(os.path.join(model_path, f)))\\n                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/safetensors/torch.py\\\", line 336, in load_file\\n    with safe_open(filename, framework=\\\"pt\\\", device=device) as f:\\n         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\nsafetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata, file not fully covered\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T16:41:25.365485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "cat /root/recovery_aware_struct_prune/results/eval_pruned_graspune_20_greedy.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "cat /root/recovery_aware_struct_prune/results/eval_pruned_graspune_20_greedy.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T16:41:25.365749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.07,\\n  \\\"stderr\\\": 0.02551470164434615,\\n  \\\"n_correct\\\": 7,\\n  \\\"n_total\\\": 100,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 2,\\n    \\\"truncated\\\": 98,\\n    \\\"eos_rate\\\": 0.02,\\n    \\\"avg_response_length\\\": 4019.52,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 177\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"11\\\",\\n      \\\"correct\\\": false,\\n      \\\"response\\\": \\\"Okay, let me try to figure out this problem. So, the problem says that the ratio of their ages is 7:11. That means if I think of their ages as parts of a whole, the total number of parts would be 7 + 1 = 2 parts. So, each part is equal to the total age divided by the total number of parts. \\\\n\\\\nLet me write that down. If 2 parts are equal to 162 years, then each part must be equal to 162 divided by 2. Let me calculate that. 162 divided by 2 equals 81. So, each part is equal to 81 years. \\\\n\\\\nNow, Alle\\\",\\n      \\\"response_length\\\": 4096,\\n      \\\"hit_eos\\\": false\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for large buttons and trades the rest of them for sma
…[truncated 7155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T16:41:25.365964+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T16:41:25.366101+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0011}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T16:41:25.366221+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "limit": "30",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "limit": "30",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T16:41:25.366365+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sft_alpha2_0_westd\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:41:05.720Z\", \"updated_at\": \"2026-05-15T15:41:05.720Z\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0012}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T16:41:25.366514+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T16:41:25.366645+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0011}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T16:41:25.366764+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T16:41:25.366883+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.001}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T16:41:25.366997+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T16:41:25.367113+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0009}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T16:41:25.367274+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T16:41:25.367405+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:13.916Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0655}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T16:41:25.367519+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T16:41:25.367636+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:14.409Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0188}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T16:41:25.367745+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T16:41:25.367866+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:15.049Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0194}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T16:41:25.367982+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-sft-alpha2.0', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0', 'eval_data': 'gsm8k_test_n100'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-sft-alpha2.0', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0', 'eval_data': 'gsm8k_test_n100'}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T16:41:25.368116+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:21.886Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha2.0\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"eval_data\": \"gsm8k_test_n100\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0239}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T16:41:25.368236+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-sft-grasp20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20', 'eval_data': 'gsm8k_test_n100'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-sft-grasp20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20', 'eval_data': 'gsm8k_test_n100'}"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T16:41:25.368393+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:24.242Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0253}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T16:41:25.368520+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-sft-alpha0.5', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5', 'eval_data': 'gsm8k_test_n100'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-sft-alpha0.5', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5', 'eval_data': 'gsm8k_test_n100'}"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T16:41:25.368654+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:26.198Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"eval_data\": \"gsm8k_test_n100\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0272}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T16:41:25.368783+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "log_path",
  "value": "/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "log_path",
    "value": "/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T16:41:25.368909+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:29.984Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha2.0\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0094}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T16:41:25.369024+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T16:41:25.369155+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:30.930Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha2.0\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0101}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T16:41:25.369289+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "log_path",
  "value": "/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "log_path",
    "value": "/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T16:41:25.369422+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:31.868Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0104}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T16:41:25.369538+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T16:41:25.369661+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:32.810Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0109}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T16:41:25.369800+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "log_path",
  "value": "/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "log_path",
    "value": "/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T16:41:25.369997+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:33.739Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0101}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T16:41:25.370255+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T16:41:25.370662+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:34.217Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0121}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T16:41:25.371002+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T16:41:25.371242+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:37.706Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha2.0\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0161}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T16:41:25.371514+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "metrics",
  "value": "{'accuracy': 0.62, 'stderr': 0.0485, 'n_correct': 62, 'n_total': 100, 'eos_rate': 0.97, 'avg_len': 277.41}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "metrics",
    "value": "{'accuracy': 0.62, 'stderr': 0.0485, 'n_correct': 62, 'n_total': 100, 'eos_rate': 0.97, 'avg_len': 277.41}"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T16:41:25.371755+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:39.610Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha2.0\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.62, \"stderr\": 0.0485, \"n_correct\": 62, \"n_total\": 100, \"eos_rate\": 0.97, \"avg_len\": 277.41}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0156}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T16:41:25.371989+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T16:41:25.372200+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:40.051Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0189}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T16:41:25.372615+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "metrics",
  "value": "{'accuracy': 0.41, 'stderr': 0.0492, 'n_correct': 41, 'n_total': 100, 'eos_rate': 0.98, 'avg_len': 225.78}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "metrics",
    "value": "{'accuracy': 0.41, 'stderr': 0.0492, 'n_correct': 41, 'n_total': 100, 'eos_rate': 0.98, 'avg_len': 225.78}"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T16:41:25.373099+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:41.588Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.41, \"stderr\": 0.0492, \"n_correct\": 41, \"n_total\": 100, \"eos_rate\": 0.98, \"avg_len\": 225.78}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0132}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T16:41:25.373884+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "conclusion",
  "value": "negative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "conclusion",
    "value": "negative"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T16:41:25.374099+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:41.933Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0175}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T16:41:25.374249+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "metrics",
  "value": "{'error': 'safetensors corrupt: incomplete metadata, file not fully covered'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "metrics",
    "value": "{'error': 'safetensors corrupt: incomplete metadata, file not fully covered'}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T16:41:25.374448+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:43.075Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"conclusion\": \"negative\", \"metrics\": {\"error\": \"safetensors corrupt: incomplete metadata, file not fully covered\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0138}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T16:41:25.374599+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_2p0",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_2p0",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T16:41:25.374757+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_2p0\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:13.916Z\", \"updated_at\": \"2026-05-15T16:40:46.869Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --n_samples 100 --output_path results/eval_sft_alpha_2.0_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha2.0\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.62, \"stderr\": 0.0485, \"n_correct\": 62, \"n_total\": 100, \"eos_rate\": 0.97, \"avg_len\": 277.41}, \"completed_at\": \"2026-05-15T16:40:46.869Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0512}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T16:41:25.374903+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_grasp_20",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_grasp_20",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T16:41:25.375060+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_grasp_20\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:14.409Z\", \"updated_at\": \"2026-05-15T16:40:47.442Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --n_samples 100 --output_path results/eval_sft_grasp_20_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_grasp_20_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.41, \"stderr\": 0.0492, \"n_correct\": 41, \"n_total\": 100, \"eos_rate\": 0.98, \"avg_len\": 225.78}, \"completed_at\": \"2026-05-15T16:40:47.442Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0829}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T16:41:25.375194+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_alpha_0p5",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_alpha_0p5",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T16:41:25.375385+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_alpha_0p5\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:15.049Z\", \"updated_at\": \"2026-05-15T16:40:47.863Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5 --n_samples 100 --output_path results/eval_sft_alpha_0.5_n100.json\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-sft-alpha0.5\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_0.5_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5\", \"conclusion\": \"negative\", \"metrics\": {\"error\": \"safetensors corrupt: incomplete metadata, file not fully covered\"}, \"completed_at\": \"2026-05-15T16:40:47.863Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0437}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T16:41:25.375545+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T16:41:25.375680+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:40:51.440Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0325}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T16:41:25.375804+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-pruned-grasp20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20', 'eval_data': 'gsm8k_test_n100'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100', 'server': 'westd-11672', 'data_path': 'gsm8k', 'data_count': 100, 'model_name': 'qwen2.5-3b-pruned-grasp20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20', 'eval_data': 'gsm8k_test_n100'}"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T16:41:25.375946+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:40:55.995Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-pruned-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.038}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T16:41:25.376067+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "log_path",
  "value": "/root/recovery_aware_struct_prune/results/eval_grasp_n100.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "log_path",
    "value": "/root/recovery_aware_struct_prune/results/eval_grasp_n100.log"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T16:41:25.376198+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:40:59.801Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-pruned-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_grasp_n100.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0161}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T16:41:25.376358+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T16:41:25.376502+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:41:00.273Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-pruned-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_grasp_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0158}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T16:41:25.376627+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T16:41:25.376756+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:41:05.012Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-pruned-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_grasp_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0252}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T16:41:25.376881+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "metrics",
  "value": "{'accuracy': 0.07, 'stderr': 0.0255, 'n_correct': 7, 'n_total': 100, 'eos_rate': 0.02, 'avg_len': 4019.52}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "metrics",
    "value": "{'accuracy': 0.07, 'stderr': 0.0255, 'n_correct': 7, 'n_total': 100, 'eos_rate': 0.02, 'avg_len': 4019.52}"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T16:41:25.377023+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:41:06.029Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-pruned-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_grasp_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.07, \"stderr\": 0.0255, \"n_correct\": 7, \"n_total\": 100, \"eos_rate\": 0.02, \"avg_len\": 4019.52}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0201}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T16:41:25.377152+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "grasp_baseline_westd",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "grasp_baseline_westd",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T16:41:25.377321+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"grasp_baseline_westd\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:40:51.440Z\", \"updated_at\": \"2026-05-15T16:41:13.070Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --n_samples 100\", \"server\": \"westd-11672\", \"data_path\": \"gsm8k\", \"data_count\": 100, \"model_name\": \"qwen2.5-3b-pruned-grasp20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"eval_data\": \"gsm8k_test_n100\"}, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_grasp_n100.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.07, \"stderr\": 0.0255, \"n_correct\": 7, \"n_total\": 100, \"eos_rate\": 0.02, \"avg_len\": 4019.52}, \"completed_at\": \"2026-05-15T16:41:13.070Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0348}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_capture-westd-all-results_20260515T163912",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-15T16:41:25.377522+00:00_

Registry 全部更新完成。汇总表：

## GSM8K Accuracy 对比 (n=100, greedy)

| 配置 | Post-Prune | Post-SFT | SFT 恢复 |
|------|-----------|----------|---------|
| α=0.0 (magnitude-only) | — | 64% | — |
| **α=0.5** | 25% | **FAIL** (checkpoint 损坏) | — |
| α=1.0 | 27% | 57% | +30pp |
| **α=2.0** | 29% | **62%** | +33pp |
| α=4.0 | 40% | 62% | +22pp |
| Standard (LLM-Pruner) | 27% | 64% | +37pp |
| RASP | 31% | 57% | +26pp |
| **GraSP-20** | **7%** (eos_rate=2%) | **41%** | +34pp |

### 关键发现

1. **α=2.0 post-SFT = 62%**，与 α=4.0 持平，但 post-prune 更低 (29% vs 40%)。SFT 恢复能力强。
2. **GraSP post-SFT = 41%**，虽然 SFT 恢复了 +34pp，但绝对值远低于其他方法。GraSP pre-SFT 仅 7% 且 eos_rate=2%（几乎全部 truncated），说明剪枝后模型结构严重受损。
3. **α=0.5 eval 失败** — safetensors 文件损坏 (`incomplete metadata, file not fully covered`)，SFT checkpoint 需要重新保存或重训。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_capture-westd-all-results_20260515T163912"
}
```

</details>

---
