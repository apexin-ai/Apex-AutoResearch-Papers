# analysis codellama13b loop only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_codellama13b_loop_only_seed42_20260519T185221.jsonl`
- **Structured JSON:** [`b59161cb641639ba4764.json`](../../sessions/b5/b59161cb641639ba4764.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-19T18:53:16.417702+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T18:53:16.418034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T18:53:16.418277+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T18:53:16.418437+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "tail -100 /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "tail -100 /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T18:53:16.418605+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"loop_only\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.7705882352941177,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": 0.055462184873949605,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 0.9152298850574713,\\n    \\\"pass_recall\\\": 0.7485311398354877,\\n    \\\"pass_f1\\\": 0.823529411764706,\\n    \\\"fail_precision\\\": 0.5668016194331984,\\n    \\\"fail_recall\\\": 0.8259587020648967,\\n    \\\"fail_f1\\\": 0.6722689075630252\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.7487394957983193,\\n    \\\"accuracy_ci_upper\\\": 0.7941176470588235,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": 0.021008403361344463,\\n    \\\"lift_ci_upper\\\": 0.09159663865546219,\\n    \\\"pass_precision_ci_lower\\\": 0.8953323903818954,\\n    \\\"pass_precision_ci_upper\\\": 0.9351730739931948,\\n    \\\"pass_recall_ci_lower\\\": 0.7186706327277261,\\n    \\\"pass_recall_ci_upper\\\": 0.7756065624899174,\\n    \\\"pass_f1_ci_lower\\\": 0.8029389671486783,\\n    \\\"pass_f1_ci_upper\\\": 0.8435738410931931,\\n    \\\"fail_precision_ci_lower\\\": 0.52528578557894,\\n    \\\"fail_precision_ci_upper\\\": 0.6100647320607598,\\n    \\\"fail_recall_ci_lower\\\": 0.7891435848455907,\\n    \\\"fail_recall_ci_upper\\\": 0.8643621265540916,\\n    \\\"fail_f1_ci_lower\\\": 0.6371463714637147,\\n    \\\"fail_f1_ci_upper\\\": 0.7068952405366146\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T18:53:16.418749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls -la /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls -la /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T18:53:16.418939+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Setting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-end generation.\\nSetting `pad_token_id` to `eos_token_id`:2 for open-en
…[truncated 3911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T18:53:16.419103+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 248700\\ndrwxr-xr-x 2 root root      4096 May 20 02:50 .\\ndrwxr-xr-x 7 root root       142 May 20 02:46 ..\\n-rw-r--r-- 1 root root      5264 May 20 02:46 README.md\\n-rw-r--r-- 1 root root      1128 May 20 02:46 adapter_config.json\\n-rw-r--r-- 1 root root 250422888 May 20 02:46 adapter_model.safetensors\\n-rw-r--r-- 1 root root       813 May 20 02:46 chat_template.jinja\\n-rw-r--r-- 1 root root      1432 May 20 02:50 eval_results.json\\n-rw-r--r-- 1 root root     77430 May 20 02:50 predictions.jsonl\\n-rw-r--r-- 1 root root       538 May 20 02:46 special_tokens_map.json\\n-rw-r--r-- 1 root root   3620731 May 20 02:46 tokenizer.json\\n-rw-r--r-- 1 root root    500058 May 20 02:46 tokenizer.model\\n-rw-r--r-- 1 root root      1869 May 20 02:46 tokenizer_config.json\\n-rw-r--r-- 1 root root      6481 May 20 02:46 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:53:16.419285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "grep -E \"step|loss|epoch|ERROR|FAIL|OOM|Traceback|completed|wandb\" /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "grep -E \"step|loss|epoch|ERROR|FAIL|OOM|Traceback|completed|wandb\" /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:53:16.419427+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T18:53:16.419549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "grep -E \"step|loss|epoch|ERROR|FAIL|OOM|Traceback|completed|wandb\" /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "grep -E \"step|loss|epoch|ERROR|FAIL|OOM|Traceback|completed|wandb\" /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:53:16.419670+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T18:53:16.419788+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "grep -n \"loss\" /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "grep -n \"loss\" /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:53:16.420009+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3:Label-only loss: False\\n16:\\r  0%|          | 0/444 [00:00<?, ?it/s]\\r  0%|          | 1/444 [00:30<3:46:16, 30.65s/it]\\r  0%|          | 2/444 [01:00<3:42:36, 30.22s/it]\\r  1%|          | 3/444 [01:30<3:42:15, 30.24s/it]\\r  1%|          | 4/444 [01:59<3:36:39, 29.54s/it]\\r  1%|          | 5/444 [02:27<3:31:16, 28.88s/it]\\r  1%|▏         | 6/444 [02:56<3:33:16, 29.22s/it]\\r  2%|▏         | 7/444 [03:27<3:37:17, 29.83s/it]\\r  2%|▏         | 8/444 [03:56<3:34:14, 29.48s/it]\\r  2%|▏         | 9/444 [04:25<3:31:44, 29.21s/it]\\r  2%|▏         | 10/444 [04:52<3:27:48, 28.73s/it]\\r                                                  \\r\\r  2%|▏         | 10/444 [04:52<3:27:48, 28.73s/it]\\r  2%|▏         | 11/444 [05:20<3:25:07, 28.42s/it]\\r  3%|▎         | 12/444 [05:50<3:28:24, 28.94s/it]\\r  3%|▎         | 13/444 [06:18<3:25:37, 28.62s/it]\\r  3%|▎         | 14/444 [06:45<3:20:25, 27.97s/it]\\r  3%|▎         | 15/444 [07:16<3:26:11, 28.84s/it]\\r  4%|▎         | 16/444 [07:47<3:30:47, 29.55s/it]\\r  4%|▍         | 17/444 [08:13<3:24:16, 28.70s/it]\\r  4%|▍         | 18/444 [08:43<3:25:56, 29.01s/it]\\r  4%|▍         | 19/444 [09:10<3:20:44, 28.34s/it]\\r  5%|▍         | 20/444 [09:39<3:21:51, 28.56s/it]\\r                                                  \\r\\r  5%|▍         | 20/444 [09:39<3:21:51, 28.56s/it]\\r  5%|▍         | 21/444 [10:03<3:12:22, 27.29s/it]\\r  5%|▍         | 22/444 [10:32<3:14:04, 27.59s/it]\\r  5%|▌         | 23/444 [11:01<3:18:12, 28.25s/it]\\r  5%|▌         | 24/444 [11:34<3:26:04, 29.44s/it]\\r  6%|▌         | 25/444 [12:06<3:32:36, 30.44s/it]\\r  6%|▌         | 26/444 [12:34<3:25:03, 29.43s/it]\\r  6%|▌         | 27/444 [12:59<3:16:44, 28.31s/it]\\r  6%|▋         | 28/444 [13:28<3:16:20, 28.32s/it]\\r  7%|▋         | 29/444 [13:59<3:22:52, 29.33s/it]\\r  7%|▋         | 30/444 [14:27<3:19:18, 28.88s/it]\\r                                                  \\r\\r  7%|▋        
…[truncated 6416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:53:16.420182+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "head -50 /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "head -50 /root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:53:16.420422+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nCondition: loop_only\\nLabel-only loss: False\\nModel: /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf\\nOutput: /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42\\nTrain: 4720, Eval: 1190\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:01<00:03,  1.69s/it]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:03<00:01,  1.65s/it]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:04<00:00,  1.36s/it]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:04<00:00,  1.44s/it]\\n\\rAdding EOS to train dataset:   0%|          | 0/4720 [00:00<?, ? examples/s]\\rAdding EOS to train dataset:  85%|████████▍ | 4000/4720 [00:00<00:00, 37758.12 examples/s]\\rAdding EOS to train dataset: 100%|██████████| 4720/4720 [00:00<00:00, 36091.74 examples/s]\\n\\rTokenizing train dataset:   0%|          | 0/4720 [00:00<?, ? examples/s]\\rTokenizing train dataset:   2%|▏         | 116/4720 [00:00<00:04, 1148.36 examples/s]\\rTokenizing train dataset:   6%|▌         | 264/4720 [00:00<00:04, 1027.86 examples/s]\\rTokenizing train dataset:   8%|▊         | 391/4720 [00:00<00:05, 801.38 examples/s] \\rTokenizing train dataset:  11%|█         | 503/4720 [00:00<00:05, 778.17 examples/s]\\rTokenizing train dataset:  13%|█▎        | 602/4720 [00:00<00:04, 832.85 examples/s]\\rTokenizing train dataset:  15%|█▍        | 690/4720 [00:00<00:04, 843.61 examples/s]\\rTokenizing train dataset:  17%|█▋        | 780/4720 [00:00<00:04, 855.37 examples/s]\\rTokenizing train dataset:  19%|█▊        | 879/4720 [00:01<00:04, 890.16 examples/s]\\rTokenizing train dataset:  21%|██        | 973/4720 [00:01<00:04, 900.43 examples/s]\\rTokenizing train dataset:  23%|██▎       | 1091/4720 [00:01<00:05, 605.61 examples/s]\\rTokenizing train dataset:  25%|██▍       | 1179/4720 [00:01<
…[truncated 6542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-19T18:53:16.420648+00:00_

## CodeLlama-13B loop_only_seed42 结果

### 核心指标

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **77.06%** | [74.87%, 79.41%] |
| Majority baseline | 71.51% | — |
| Lift over majority | +5.55pp | [+2.1pp, +9.2pp] |

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 0.92 | 0.75 | 0.82 |
| fail | 0.57 | 0.83 | 0.67 |

### 对比

| Comparison | Accuracy | Delta |
|------------|----------|-------|
| CodeLlama-13B **ae_only** | 99.08% | **-22.02pp** |
| CodeLlama-13B **loop_only** (this) | 77.06% | — |
| Qwen-7B **loop_only** | 85.63% | **-8.57pp** |
| Qwen-7B **ae_only** | 99.92% | -22.86pp |

### Hypothesis 验证

**ae_only > loop_only 跨模型成立。** CodeLlama-13B 上 ae_only (99.08%) vs loop_only (77.06%) 差距 22pp，远超预期的 ≥10pp。Tier hierarchy 在第二个模型上得到确认。

额外发现：CodeLlama-13B loop_only (77.06%) 显著低于 Qwen-7B loop_only (85.63%)，说明 CodeLlama-13B 在 loop-only traces 上的学习能力弱于 Qwen-7B。而在 ae_only 条件下两模型表现接近（99.08% vs 99.92%），差距主要体现在困难条件上。

### 训练状态

- **正常完成**，EXIT_CODE=0
- 444 steps, 3 epochs, 训练时长 ~3h45m
- Final train loss: 0.023, eval loss epoch 2: 0.131 → epoch 3: 0.145（轻微过拟合）
- Checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_loop_only_seed42/final/`
- Log: `/root/runs/trace-verdict-study/codellama13b_loop_only_seed42.log`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_codellama13b_loop_only_seed42_20260519T185221"
}
```

</details>

---
