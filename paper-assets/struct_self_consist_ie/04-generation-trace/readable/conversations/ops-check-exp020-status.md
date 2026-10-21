# ops check exp020 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_ops_check_exp020_status_20260516T121557.jsonl`
- **Structured JSON:** [`7bd89d78068628b9ace8.json`](../../sessions/7b/7bd89d78068628b9ace8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-16T12:16:44.208905+00:00_

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
  "session": "worker_ops_check_exp020_status_20260516T121557",
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

_source line 2 · 2026-05-16T12:16:44.209251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T12:16:44.209439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps aux | grep -E \"fewnerd|few-nerd|few_nerd|exp.020\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps aux | grep -E \"fewnerd|few-nerd|few_nerd|exp.020\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T12:16:44.209583+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T12:16:44.209710+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T12:16:44.209833+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T12:16:44.209983+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sat May 16 20:16:16 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 5090        On  |   00000000:38:00.0 Off |                  N/A |\\n| 42%   30C    P8             12W /  575W |       2MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 5090        On  |   00000000:49:00.0 Off |                  N/A |\\n| 68%   73C    P1            438W /  575W |   27720MiB /  32607MiB |     99%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 5090        On  |   00000000:5A:00.0 Off |                  N/A |\\n| 42%   28C    P8             14W /  575W |       2MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 5090        On  |   00000000:98:00.0 Off |                  N/A |\\n| 39%   29C    P8             
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T12:16:44.210158+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T12:16:44.210317+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.log\" -newer /root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.log\" -newer /root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T12:16:44.210447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/fewnerd_train.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T12:16:44.210569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T12:16:44.210702+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp017_train.log\\nfewnerd_train.log\\nft_001_train.log\\nft_fewnerd_smoke\\nllama3.1-8b-conll2003-lora\\nllama3.1-8b-conll2003-merged\\nllama3.1-8b-scierc-lora\\nllama3.1-8b-scierc-merged\\nllama3.2-3b-scierc-lora\\nllama3.2-3b-scierc-merged\\nqwen3-4b-conll2003-lora\\nqwen3-4b-conll2003-merged\\nqwen3-4b-conll2003-merged-ckpt4200\\nqwen3-4b-scierc-lora\\nqwen3-4b-scierc-merged\\nqwen3-8b-conll2003-lora\\nqwen3-8b-conll2003-merged\\nqwen3-8b-scierc-lora-rank8\\nqwen3-8b-scierc-lora-v2\\nqwen3-8b-scierc-merged-rank8\\nqwen3-8b-scierc-merged-v2\\nqwen3-8b-wnut17-lora\\nqwen3-8b-wnut17-merged\\nwnut17_train.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T12:16:44.210828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"nohup*\" -newer /root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"nohup*\" -newer /root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T12:16:44.210951+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:16:44.211068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -50 /root/autodl-tmp/struct_self_consist_ie/checkpoints/fewnerd_train.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -50 /root/autodl-tmp/struct_self_consist_ie/checkpoints/fewnerd_train.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T12:16:44.211367+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\",\\n    \\\"full_attention\\\"\\n  ],\\n  \\\"max_position_embeddings\\\": 40960,\\n  \\\"max_window_layers\\\": 36,\\n  \\\"model_type\\\": \\\"qwen3\\\",\\n  \\\"num_attention_heads\\\": 32,\\n  \\\"num_hidden_layers\\\": 36,\\n  \\\"num_key_value_heads\\\": 8,\\n  \\\"rms_norm_eps\\\": 1e-06,\\n  \\\"rope_scaling\\\": null,\\n  \\\"rope_theta\\\": 1000000,\\n  \\\"sliding_window\\\": null,\\n  \\\"tie_word_embeddings\\\": false,\\n  \\\"transformers_version\\\": \\\"4.57.1\\\",\\n  \\\"use_cache\\\": true,\\n  \\\"use_sliding_window\\\": false,\\n  \\\"vocab_size\\\": 151936\\n}\\n\\n[INFO|tokenization_utils_base.py:2421] 2026-05-16 19:56:12,701 >> chat template saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/checkpoint-2000/chat_template.jinja\\n[INFO|tokenization_utils_base.py:2590] 2026-05-16 19:56:12,701 >> tokenizer config file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/checkpoint-2000/tokenizer_config.json\\n[INFO|tokenization_utils_base.py:2599] 2026-05-16 19:56:12,701 >> Special tokens file saved in /root/autodl-tmp/struct_self_consist_ie/checkpo
…[truncated 6798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T12:16:44.211559+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T12:16:44.211697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoint-1000\\ncheckpoint-2000\\ntrainer_log.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T12:16:44.211837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/trainer_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/trainer_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T12:16:44.212043+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"current_steps\\\": 1700, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0686, \\\"lr\\\": 0.0001932012136445065, \\\"epoch\\\": 0.20642341084330035, \\\"percentage\\\": 20.64, \\\"elapsed_time\\\": \\\"1:05:42\\\", \\\"remaining_time\\\": \\\"4:12:38\\\"}\\n{\\\"current_steps\\\": 1750, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0678, \\\"lr\\\": 0.00019241226476058088, \\\"epoch\\\": 0.21249468763280918, \\\"percentage\\\": 21.25, \\\"elapsed_time\\\": \\\"1:07:21\\\", \\\"remaining_time\\\": \\\"4:09:37\\\"}\\n{\\\"current_steps\\\": 1800, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0663, \\\"lr\\\": 0.0001915818126089219, \\\"epoch\\\": 0.21856596442231802, \\\"percentage\\\": 21.86, \\\"elapsed_time\\\": \\\"1:08:59\\\", \\\"remaining_time\\\": \\\"4:06:40\\\"}\\n{\\\"current_steps\\\": 1850, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0683, \\\"lr\\\": 0.00019071023015385504, \\\"epoch\\\": 0.22463724121182685, \\\"percentage\\\": 22.46, \\\"elapsed_time\\\": \\\"1:10:38\\\", \\\"remaining_time\\\": \\\"4:03:50\\\"}\\n{\\\"current_steps\\\": 1900, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0666, \\\"lr\\\": 0.00018979790883173422, \\\"epoch\\\": 0.23070851800133568, \\\"percentage\\\": 23.07, \\\"elapsed_time\\\": \\\"1:12:17\\\", \\\"remaining_time\\\": \\\"4:01:05\\\"}\\n{\\\"current_steps\\\": 1950, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0664, \\\"lr\\\": 0.0001888452583751442, \\\"epoch\\\": 0.23677979479084452, \\\"percentage\\\": 23.68, \\\"elapsed_time\\\": \\\"1:13:56\\\", \\\"remaining_time\\\": \\\"3:58:22\\\"}\\n{\\\"current_steps\\\": 2000, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.0671, \\\"lr\\\": 0.0001878527066288851, \\\"epoch\\\": 0.24285107158035335, \\\"percentage\\\": 24.28, \\\"elapsed_time\\\": \\\"1:15:35\\\", \\\"remaining_time\\\": \\\"3:55:41\\\"}\\n{\\\"current_steps\\\": 2000, \\\"total_steps\\\": 8236, \\\"eval_loss\\\": 0.06579617410898209, \\\"epoch\\\": 0.24285107158035
…[truncated 3321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T12:16:44.212224+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/trainer_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/trainer_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T12:16:44.212383+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"current_steps\\\": 50, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.9598, \\\"lr\\\": 1.1893203883495147e-05, \\\"epoch\\\": 0.006071276789508834, \\\"percentage\\\": 0.61, \\\"elapsed_time\\\": \\\"0:01:37\\\", \\\"remaining_time\\\": \\\"4:25:41\\\"}\\n{\\\"current_steps\\\": 100, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.2143, \\\"lr\\\": 2.4029126213592234e-05, \\\"epoch\\\": 0.012142553579017668, \\\"percentage\\\": 1.21, \\\"elapsed_time\\\": \\\"0:03:15\\\", \\\"remaining_time\\\": \\\"4:24:28\\\"}\\n{\\\"current_steps\\\": 150, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.1711, \\\"lr\\\": 3.616504854368932e-05, \\\"epoch\\\": 0.0182138303685265, \\\"percentage\\\": 1.82, \\\"elapsed_time\\\": \\\"0:04:52\\\", \\\"remaining_time\\\": \\\"4:22:40\\\"}\\n{\\\"current_steps\\\": 200, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.1558, \\\"lr\\\": 4.830097087378641e-05, \\\"epoch\\\": 0.024285107158035335, \\\"percentage\\\": 2.43, \\\"elapsed_time\\\": \\\"0:06:27\\\", \\\"remaining_time\\\": \\\"4:19:28\\\"}\\n{\\\"current_steps\\\": 250, \\\"total_steps\\\": 8236, \\\"loss\\\": 0.1386, \\\"lr\\\": 6.043689320388349e-05, \\\"epoch\\\": 0.03035638394754417, \\\"percentage\\\": 3.04, \\\"elapsed_time\\\": \\\"0:08:05\\\", \\\"remaining_time\\\": \\\"4:18:34\\\"}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_exp020_status_20260516T121557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T12:16:44.212581+00:00_

## exp-020 Few-NERD Smoke Test 状态

**训练仍在进行中**，PID 288683，GPU 1 (RTX 5090, 27710MiB / 99% util)。

| 指标 | 值 |
|------|-----|
| 进度 | 2622 / 8236 steps (31.8%) |
| Epoch | ~0.32 |
| 已运行 | ~1h46m |
| 预计剩余 | ~3h03m |
| 当前 loss | 0.0603 (step 2600) |
| Eval loss (step 2000) | 0.0658 |
| 速度 | ~1.95 s/it |

**Loss 曲线**：从 0.96 (step 50) → 0.21 (step 100) → 0.07 (step 1700) → 0.06 (step 2600)，收敛正常。

**Checkpoints 已保存**：`checkpoint-1000`, `checkpoint-2000` 在 `/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/`

预计约 3 小时后训练完成。尚无 inference 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_check_exp020_status_20260516T121557"
}
```

</details>

---
