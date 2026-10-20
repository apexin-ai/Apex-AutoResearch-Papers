# analysis v4 taxei fixed inject10 s7

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048.jsonl`
- **Structured JSON:** [`bae4d54de8a9a9930e94.json`](../../sessions/ba/bae4d54de8a9a9930e94.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T21:01:42.530593+00:00_

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
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
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

_source line 2 · 2026-05-15T21:01:42.530958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T21:01:42.531153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find ~/output/ -name \"*.safetensors\" -path \"*taxei*\" 2>/dev/null | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find ~/output/ -name \"*.safetensors\" -path \"*taxei*\" 2>/dev/null | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T21:01:42.531298+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T21:01:42.531427+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T21:01:42.531641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"run sh: `/root/miniconda3/bin/python /root/miniconda3/lib/python3.12/site-packages/swift/cli/sft.py --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 7 --data_seed 7 --output_dir checkpoints/v4_taxei_fixed_inject10_s7 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95`\\n[INFO:swift] Successfully registered `/root/miniconda3/lib/python3.12/site-packages/swift/dataset/data/dataset_info.json`.\\nbitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n[INFO:swift] rank: -1, local_rank: -1, world_size: 1, local_world_size: 1\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n[INFO:swift] Setting torch_dtype: torch.bfloat16\\n[INFO:swift] Setting args.lazy_tokenize: False\\n[INFO:swift] Setting args.dataloader_num_workers: 1\\n[INFO:
…[truncated 2214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T21:01:42.531815+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -50 ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -50 ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T21:01:42.532024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 0.31899161, 'grad_norm': 1.70615709, 'learning_rate': 3.65e-06, 'token_acc': 0.8812724, 'epoch': 2.63, 'global_step/max_steps': '1435/1635', 'elapsed_time': '50m 10s', 'remaining_time': '6m 60s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.09774}\\n{'loss': 0.26494832, 'grad_norm': 1.31835949, 'learning_rate': 3.47e-06, 'token_acc': 0.90891283, 'epoch': 2.64, 'global_step/max_steps': '1440/1635', 'elapsed_time': '50m 21s', 'remaining_time': '6m 49s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.098055}\\n{'loss': 0.29283452, 'grad_norm': 1.2747128, 'learning_rate': 3.3e-06, 'token_acc': 0.90022371, 'epoch': 2.65, 'global_step/max_steps': '1445/1635', 'elapsed_time': '50m 31s', 'remaining_time': '6m 39s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.097779}\\n{'loss': 0.31923664, 'grad_norm': 1.40392566, 'learning_rate': 3.13e-06, 'token_acc': 0.88898377, 'epoch': 2.66, 'global_step/max_steps': '1450/1635', 'elapsed_time': '50m 43s', 'remaining_time': '6m 28s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.098328}\\n{'loss': 0.28298283, 'grad_norm': 1.67940414, 'learning_rate': 2.96e-06, 'token_acc': 0.89755422, 'epoch': 2.67, 'global_step/max_steps': '1455/1635', 'elapsed_time': '50m 53s', 'remaining_time': '6m 18s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.09848}\\n{'loss': 0.32432785, 'grad_norm': 1.52573788, 'learning_rate': 2.8e-06, 'token_acc': 0.88795124, 'epoch': 2.68, 'global_step/max_steps': '1460/1635', 'elapsed_time': '51m 4s', 'remaining_time': '6m 7s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.098474}\\n{'loss': 0.2966398, 'grad_norm': 1.50755584, 'learning_rate': 2.64e-06, 'token_acc': 0.89478542, 'epoch': 2.69, 'global_step/max_steps': '1465/1635', 'elapsed_time': '51m 15s', 'remaining_time': '5m 57s', 'memory(GiB)': 18.15, 'train_speed(s/it)': 2.098906}\\n{'loss': 0.26198647, 'grad_norm': 1.32712257, 'learning_rate': 2.49e-06, 'token_acc': 0.90649606, 'epoch': 2.7, 'global_step/m
…[truncated 6265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T21:01:42.532178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls ~/output/ | grep -i \"taxei\\|inject\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls ~/output/ | grep -i \"taxei\\|inject\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T21:01:42.532303+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T21:01:42.532455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7 -name \"*.safetensors\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7 -name \"*.safetensors\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T21:01:42.532603+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T21:01:42.532738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -i \"wandb\" ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -i \"wandb\" ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T21:01:42.532859+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T21:01:42.532983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T21:01:42.533105+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"args.json\\ncheckpoint-1090\\ncheckpoint-1635\\ncheckpoint-545\\nimages\\nlogging.jsonl\\nruns\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T21:01:42.533223+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls ~/output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls ~/output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T21:01:42.533345+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/output/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T21:01:42.533487+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T21:01:42.533643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nadditional_config.json\\nargs.json\\noptimizer.pt\\nrng_state.pth\\nscheduler.pt\\ntrainer_state.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T21:01:42.533762+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7 -name \"*.safetensors\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7 -name \"*.safetensors\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T21:01:42.533893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v0-20260516-025729/checkpoint-545/adapter_model.safetensors\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v0-20260516-025729/checkpoint-1090/adapter_model.safetensors\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v0-20260516-025729/checkpoint-1635/adapter_model.safetensors\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-545/adapter_model.safetensors\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1090/adapter_model.safetensors\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635/adapter_model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T21:01:42.534070+00:00_

## 实验 v4-taxei-fixed-inject10-s7 训练报告

| 项目 | 值 |
|------|-----|
| **checkpoint_path** | `/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635` |
| **wandb_run_id** | 无（未配置 W&B） |
| **final_train_loss** | 0.4212 (avg)，末步 loss=0.237 |
| **final_token_acc** | 0.905 (末步) |
| **total_steps** | 1635 (3 epochs) |
| **training_time** | 57m 17s (3437s) |
| **train_speed** | 2.10 s/it |
| **memory** | 18.15 GiB |

### Checkpoint 结构

3个 epoch checkpoint，均为 LoRA adapter：
- `checkpoint-545` (epoch 1)
- `checkpoint-1090` (epoch 2)  
- `checkpoint-1635` (epoch 3, 最终)

每个 checkpoint 含 `adapter_model.safetensors` + `adapter_config.json`。

### 注意事项

1. **存在两个版本**：v0 (`v0-20260516-025729`) 和 v1 (`v1-20260516-040128`)，当前完成的是 v1。v0 也有完整的 3 个 checkpoint，可能需要清理以释放磁盘空间。
2. **bitsandbytes 警告**：`libnvJitLink.so.13` 加载失败，但未影响训练（量化功能未被使用）。
3. **模型**：Qwen3-8B + LoRA rank 16，cosine lr schedule，lr=1e-4，weight_decay=0.1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048"
}
```

</details>

---
