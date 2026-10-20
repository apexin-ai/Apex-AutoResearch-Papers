# analysis exp 001 sft 14b d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054.jsonl`
- **Structured JSON:** [`adced5a568d4c612dcdb.json`](../../sessions/ad/adced5a568d4c612dcdb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-19T00:22:00.414026+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T00:22:00.414425+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T00:22:00.414650+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"nvidia-smi --query-gpu=index,name,memory.total --format=csv,noheader\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"nvidia-smi --query-gpu=index,name,memory.total --format=csv,noheader\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T00:22:00.414805+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.98}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T00:22:00.414955+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T00:22:00.415083+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/.done 2>/dev/null && echo DONE || echo No_done\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/.done 2>/dev/null && echo DONE || echo No_done\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T00:22:00.415215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  3 root root   80 May 19 08:13 .\\ndrwxr-xr-x 22 root root 4096 May 19 07:29 ..\\n-rw-r--r--  1 root root    5 May 19 08:13 .done\\ndrwxr-xr-x  3 root root 4096 May 19 08:13 lora_adapter\\n-rw-r--r--  1 root root  351 May 19 08:13 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T00:22:00.415382+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/train_config.json 2>/dev/null\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/train_config.json 2>/dev/null\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T00:22:00.415531+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/.done\\nDONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T00:22:00.415654+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"/root/miniconda3/bin/python3.12 -c \\\"\nimport json\nwith open('/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/trainer_state.json') as f:\n    state = json.load(f)\nlogs = state.get('log_history', [])\nprint(f'Total logged: {len(logs)}')\nfor entry in logs[-5:]:\n    print(entry)\n\\\"\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"/root/miniconda3/bin/python3.12 -c \\\"\nimport json\nwith open('/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/trainer_state.json') as f:\n    state = json.load(f)\nlogs = state.get('log_history', [])\nprint(f'Total logged: {len(logs)}')\nfor entry in logs[-5:]:\n    print(entry)\n\\\"\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T00:22:00.415802+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"/root/autodl-tmp/models/Qwen2.5-14B\\\",\\n  \\\"data_path\\\": \\\"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\\\",\\n  \\\"lora_r\\\": 16,\\n  \\\"lora_alpha\\\": 32,\\n  \\\"epochs\\\": 1,\\n  \\\"batch_size\\\": 1,\\n  \\\"grad_accum\\\": 16,\\n  \\\"lr\\\": 5e-05,\\n  \\\"max_seq_length\\\": 2048,\\n  \\\"seed\\\": 42,\\n  \\\"num_samples\\\": 66533,\\n  \\\"gradient_checkpointing\\\": false,\\n  \\\"load_in_4bit\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T00:22:00.415934+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"Traceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 3, in &lt;module>\\nFileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/trainer_state.json'\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T00:22:00.416088+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T00:22:00.416221+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 280080\\ndrwxr-xr-x 3 root root      4096 May 19 08:13 .\\ndrwxr-xr-x 3 root root        80 May 19 08:13 ..\\n-rw-r--r-- 1 root root      1458 May 19 08:13 README.md\\n-rw-r--r-- 1 root root      1114 May 19 08:13 adapter_config.json\\n-rw-r--r-- 1 root root 275341720 May 19 08:13 adapter_model.safetensors\\n-rw-r--r-- 1 root root      2427 May 19 08:13 chat_template.jinja\\ndrwxr-xr-x 2 root root      4096 May 19 08:13 checkpoint-4159\\n-rw-r--r-- 1 root root  11421892 May 19 08:13 tokenizer.json\\n-rw-r--r-- 1 root root       696 May 19 08:13 tokenizer_config.json\\n-rw-r--r-- 1 root root      5777 May 19 08:13 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T00:22:00.416410+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/checkpoint-4159/\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/checkpoint-4159/\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T00:22:00.416582+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/adapter_config.json\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/adapter_config.json\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T00:22:00.416715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nchat_template.jinja\\noptimizer.pt\\nrng_state.pth\\nscheduler.pt\\ntokenizer.json\\ntokenizer_config.json\\ntrainer_state.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T00:22:00.416878+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/models/Qwen2.5-14B\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 32,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.1\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 16,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"k_proj\\\",\\n    \\\"gate_proj\\\",\\n    \\\"up_proj\\\",\\n    \\\"v_proj\\\",\\n    \\\"q_proj\\\",\\n    \\\"down_proj\\\",\\n    \\\"o_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T00:22:00.417037+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"/root/miniconda3/bin/python3.12 -c \\\"\nimport json\nwith open('/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/checkpoint-4159/trainer_state.json') as f:\n    state = json.load(f)\nlogs = state.get('log_history', [])\nprint(f'Total logged: {len(logs)}')\nprint(f'total_flos: {state.get(\\\\\\\"total_flos\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'best_metric: {state.get(\\\\\\\"best_metric\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'global_step: {state.get(\\\\\\\"global_step\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'max_steps: {state.get(\\\\\\\"max_steps\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'epoch: {state.get(\\\\\\\"epoch\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint('--- Last 5 logs ---')\nfor entry in logs[-5:]:\n    print(entry)\n\\\"\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ssh -p 29999 root@connect.westd.seetacloud.com \"/root/miniconda3/bin/python3.12 -c \\\"\nimport json\nwith open('/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/checkpoint-4159/trainer_state.json') as f:\n    state = json.load(f)\nlogs = state.get('log_history', [])\nprint(f'Total logged: {len(logs)}')\nprint(f'total_flos: {state.get(\\\\\\\"total_flos\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'best_metric: {state.get(\\\\\\\"best_metric\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'global_step: {state.get(\\\\\\\"global_step\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'max_steps: {state.get(\\\\\\\"max_steps\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint(f'epoch: {state.get(\\\\\\\"epoch\\\\\\\", \\\\\\\"N/A\\\\\\\")}')\nprint('--- Last 5 logs ---')\nfor entry in logs[-5:]:\n    print(entry)\n\\\"\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T00:22:00.417193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total logged: 415\\ntotal_flos: 1.820108825182544e+18\\nbest_metric: None\\nglobal_step: 4159\\nmax_steps: 4159\\nepoch: 1.0\\n--- Last 5 logs ---\\n{'entropy': 1.06842694375664, 'epoch': 0.9883817053191649, 'grad_norm': 0.2633078396320343, 'learning_rate': 1.975506680421957e-08, 'loss': 0.9396921157836914, 'mean_token_accuracy': 0.7609978720545769, 'num_tokens': 21346294.0, 'step': 4110}\\n{'entropy': 1.1957056007348001, 'epoch': 0.9907865269866082, 'grad_norm': 0.24968840181827545, 'learning_rate': 1.264384230428295e-08, 'loss': 1.0605484008789063, 'mean_token_accuracy': 0.7359029691666364, 'num_tokens': 21392259.0, 'step': 4120}\\n{'entropy': 1.0753994920291006, 'epoch': 0.9931913486540513, 'grad_norm': 0.3381637930870056, 'learning_rate': 7.112423607946728e-09, 'loss': 0.9573508262634277, 'mean_token_accuracy': 0.7629606544971466, 'num_tokens': 21438252.0, 'step': 4130}\\n{'entropy': 1.1022405874915422, 'epoch': 0.9955961703214946, 'grad_norm': 0.23753304779529572, 'learning_rate': 3.161160434775323e-09, 'loss': 0.9974279403686523, 'mean_token_accuracy': 0.7525958731770516, 'num_tokens': 21486628.0, 'step': 4140}\\n{'entropy': 1.1178546086885035, 'epoch': 0.9980009919889378, 'grad_norm': 0.3089064061641693, 'learning_rate': 7.903026002592517e-10, 'loss': 1.0002406120300293, 'mean_token_accuracy': 0.7527597863227129, 'num_tokens': 21535187.0, 'step': 4150}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T00:22:00.417388+00:00_

## 14B d100 s42 训练结果

| 项目 | 值 |
|---|---|
| **结论** | **SUCCESS** |
| .done | 存在 |
| total_steps | 4159/4159 (100%) |
| epoch | 1.0 |
| final_loss | ~1.000 (step 4150) |
| final_token_accuracy | ~0.753 (step 4150) |
| lora_alpha | 32 (符合规范) |
| lora_r | 16 |
| lr | 5e-5 |
| num_samples | 66,533 |
| batch_size | 1 × grad_accum 16 |
| adapter 大小 | 275MB |

训练正常完成，loss 在 0.94–1.06 区间波动，token accuracy 稳定在 0.75 附近，lr 已衰减至接近零。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054"
}
```

</details>

---
