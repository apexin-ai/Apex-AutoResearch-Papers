# ops check old server checkpoint

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_ops_check-old-server-checkpoint_20260523T124311.jsonl`
- **Structured JSON:** [`6d669d2b4b1c321d7158.json`](../../sessions/6d/6d669d2b4b1c321d7158.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-23T12:43:57.047847+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T12:43:57.048349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T12:43:57.048633+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"19912\" ~/.ssh/config 2>/dev/null || echo \"NOT_IN_SSH_CONFIG\"",
  "description": "Check SSH config for server 19912"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"19912\" ~/.ssh/config 2>/dev/null || echo \"NOT_IN_SSH_CONFIG\"",
    "description": "Check SSH config for server 19912"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T12:43:57.048854+00:00_

NOT_IN_SSH_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T12:43:57.049061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T12:43:57.049271+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '||' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T12:43:57.049508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T12:43:57.049729+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 64\\ndrwxr-xr-x 16 root root 4096 May 22 18:06 .\\ndrwxr-xr-x  7 root root 4096 May 22 18:05 ..\\ndrwxr-xr-x  5 root root 4096 May 21 05:15 clean\\ndrwxr-xr-x  5 root root 4096 May 21 21:21 clean_s10\\ndrwxr-xr-x  5 root root 4096 May 21 07:56 clean_s2\\ndrwxr-xr-x  5 root root 4096 May 21 07:40 clean_s3\\ndrwxr-xr-x  5 root root 4096 May 21 20:09 clean_s4\\ndrwxr-xr-x  5 root root 4096 May 21 20:09 clean_s5\\ndrwxr-xr-x  5 root root 4096 May 21 20:10 clean_s6\\ndrwxr-xr-x  5 root root 4096 May 21 20:11 clean_s7\\ndrwxr-xr-x  5 root root 4096 May 21 21:21 clean_s8\\ndrwxr-xr-x  5 root root 4096 May 21 21:21 clean_s9\\ndrwxr-xr-x  5 root root 4096 May 21 05:27 contam_15\\ndrwxr-xr-x  5 root root 4096 May 22 13:47 contam_25\\ndrwxr-xr-x  5 root root 4096 May 22 18:26 contam_5\\ndrwxr-xr-x  5 root root 4096 May 21 05:48 contam_50\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T12:43:57.049956+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T12:43:57.050167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 43516\\ndrwxr-xr-x  5 root root     4096 May 21 05:15 .\\ndrwxr-xr-x 16 root root     4096 May 22 18:06 ..\\n-rw-r--r--  1 root root     1504 May 21 05:15 README.md\\n-rw-r--r--  1 root root     1095 May 21 05:15 adapter_config.json\\n-rw-r--r--  1 root root 27297544 May 21 05:15 adapter_model.safetensors\\n-rw-r--r--  1 root root     4614 May 21 05:15 chat_template.jinja\\ndrwxr-xr-x  2 root root     4096 May 21 05:04 checkpoint-313\\ndrwxr-xr-x  2 root root     4096 May 21 05:09 checkpoint-626\\ndrwxr-xr-x  2 root root     4096 May 21 05:15 checkpoint-939\\n-rw-r--r--  1 root root 17209920 May 21 05:15 tokenizer.json\\n-rw-r--r--  1 root root      353 May 21 05:15 tokenizer_config.json\\n-rw-r--r--  1 root root     5777 May 21 05:15 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T12:43:57.050405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/contam_15/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/contam_15/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T12:43:57.050634+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 43516\\ndrwxr-xr-x  5 root root     4096 May 21 05:27 .\\ndrwxr-xr-x 16 root root     4096 May 22 18:06 ..\\n-rw-r--r--  1 root root     1512 May 21 05:27 README.md\\n-rw-r--r--  1 root root     1095 May 21 05:27 adapter_config.json\\n-rw-r--r--  1 root root 27297544 May 21 05:27 adapter_model.safetensors\\n-rw-r--r--  1 root root     4614 May 21 05:27 chat_template.jinja\\ndrwxr-xr-x  2 root root     4096 May 21 05:27 checkpoint-1335\\ndrwxr-xr-x  2 root root     4096 May 21 05:09 checkpoint-445\\ndrwxr-xr-x  2 root root     4096 May 21 05:18 checkpoint-890\\n-rw-r--r--  1 root root 17209920 May 21 05:27 tokenizer.json\\n-rw-r--r--  1 root root      353 May 21 05:27 tokenizer_config.json\\n-rw-r--r--  1 root root     5841 May 21 05:27 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T12:43:57.050846+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/contam_50/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "ls -la /root/autodl-tmp/ctrl_contam_llama/checkpoints/contam_50/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T12:43:57.051042+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "du -sh /root/autodl-tmp/ctrl_contam_llama/checkpoints/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "du -sh /root/autodl-tmp/ctrl_contam_llama/checkpoints/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T12:43:57.051251+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 43516\\ndrwxr-xr-x  5 root root     4096 May 21 05:48 .\\ndrwxr-xr-x 16 root root     4096 May 22 18:06 ..\\n-rw-r--r--  1 root root     1512 May 21 05:48 README.md\\n-rw-r--r--  1 root root     1095 May 21 05:48 adapter_config.json\\n-rw-r--r--  1 root root 27297544 May 21 05:48 adapter_model.safetensors\\n-rw-r--r--  1 root root     4614 May 21 05:48 chat_template.jinja\\ndrwxr-xr-x  2 root root     4096 May 21 05:32 checkpoint-1504\\ndrwxr-xr-x  2 root root     4096 May 21 05:48 checkpoint-2256\\ndrwxr-xr-x  2 root root     4096 May 21 05:16 checkpoint-752\\n-rw-r--r--  1 root root 17209920 May 21 05:48 tokenizer.json\\n-rw-r--r--  1 root root      353 May 21 05:48 tokenizer_config.json\\n-rw-r--r--  1 root root     5841 May 21 05:48 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T12:43:57.051493+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"4.5G\\t/root/autodl-tmp/ctrl_contam_llama/checkpoints/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T12:43:57.051719+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "cat /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean/training_args.bin",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "cat /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean/training_args.bin",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T12:43:57.052284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PK\\u0003\\u0004\\u0000\\u0000\\b\\b\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0016\\u0000\\f\\u0000training_args/data.pklFB\\b\\u0000ZZZZZZZZ�\\u0002ctrl.trainer.sft_config\\nSFTConfig\\nq\\u0000)�q\\u0001}q\\u0002(X\\n\\u0000\\u0000\\u0000output_dirq\\u0003X4\\u0000\\u0000\\u0000/root/autodl-tmp/ctrl_contam_llama/checkpoints/cleanq\\u0004X\\u001b\\u0000\\u0000\\u0000per_device_train_batch_sizeq\\u0005K\\u0004X\\u0010\\u0000\\u0000\\u0000num_train_epochsq\\u0006K\\u0003X\\t\\u0000\\u0000\\u0000max_stepsq\\u0007J����X\\r\\u0000\\u0000\\u0000learning_rateq\\bG?*6��\\u001cC-X\\u0011\\u0000\\u0000\\u0000lr_scheduler_typeq\\tctransformers.trainer_utils\\nSchedulerType\\nq\\nX\\u0006\\u0000\\u0000\\u0000linearq\\u000b�q\\fRq\\rX\\u0013\\u0000\\u0000\\u0000lr_scheduler_kwargsq\\u000eNX\\f\\u0000\\u0000\\u0000warmup_stepsq\\u000fG?�������X\\u0005\\u0000\\u0000\\u0000optimq\\u0010ctransformers.training_args\\nOptimizerNames\\nq\\u0011X\\u0011\\u0000\\u0000\\u0000adamw_torch_fusedq\\u0012�q\\u0013Rq\\u0014X\\n\\u0000\\u0000\\u0000optim_argsq\\u0015NX\\f\\u0000\\u0000\\u0000weight_decayq\\u0016G\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000X\\n\\u0000\\u0000\\u0000adam_beta1q\\u0017G?�������X\\n\\u0000\\u0000\\u0000adam_beta2q\\u0018G?����\\u0016�+X\\f\\u0000\\u0000\\u0000adam_epsilonq\\u0019G>Ey��0�:X\\u0014\\u0000\\u0000\\u0000optim_target_modulesq\\u001aNX\\u001b\\u0000\\u0000\\u0000gradient_accumulation_stepsq\\u001bK\\u0004X\\u001d\\u0000\\u0000\\u0000average_tokens_across_devicesq\\u001c�X\\r\\u0000\\u0000\\u0000max_grad_normq\\u001dG?�\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000X\\u0016\\u0000\\u0000\\u0000label_smoothing_factorq\\u001eG\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000X\\u0004\\u0000\\u0000\\u0000bf16q\\u001f�X\\u0004\\u0000\\u0000\\u0000fp16q �X\\u000e\\u0000\\u0000\\u0000bf16_full_evalq!�X\\u000e
…[truncated 11590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T12:43:57.052567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35694",
  "command": "cat /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean/adapter_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35694",
    "command": "cat /root/autodl-tmp/ctrl_contam_llama/checkpoints/clean/adapter_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T12:43:57.052831+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 32,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.1\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 16,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"o_proj\\\",\\n    \\\"v_proj\\\",\\n    \\\"k_proj\\\",\\n    \\\"q_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T12:43:57.053114+00:00_

从 training_args 中可以确认 `seed=42` (K* = 0x2A = 42)。所有旧 Llama s1 checkpoints 已在 westd-35694 上。

## 结果

**旧 Llama s1 (seed 42) checkpoints 已在 westd-35694 上，无需访问 19912。**

路径：`/root/autodl-tmp/ctrl_contam_llama/checkpoints/`

| 条件 | 目录 | 中间 checkpoints | adapter 大小 |
|------|------|-----------------|-------------|
| clean | `clean/` | 313, 626, 939 | 26MB |
| contam_15 | `contam_15/` | 445, 890, 1335 | 26MB |
| contam_50 | `contam_50/` | 752, 1504, 2256 | 26MB |

- 总大小：**4.5GB**（含所有 16 个子目录，包括 s2-s10 的 clean 变体和 contam_5/contam_25）
- seed 确认：training_args 中 `seed=42`
- base model：`Meta-Llama-3.1-8B-Instruct`（LoRA r=16, alpha=32）
- 19912 不在 SSH config 中，但不需要连——数据已在本地

可以直接用新代码在 westd-35694 上 re-eval 这些 checkpoint。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_check-old-server-checkpoint_20260523T124311"
}
```

</details>

---
