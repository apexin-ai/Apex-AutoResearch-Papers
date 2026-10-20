# ssh find 4b sft adapter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_ssh_find-4b-sft-adapter_20260521T073041.jsonl`
- **Structured JSON:** [`3715b1807bcec7824360.json`](../../sessions/37/3715b1807bcec7824360.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-21T07:33:25.905671+00:00_

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
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
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

_source line 2 · 2026-05-21T07:33:25.906064+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T07:33:25.907268+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_output*4b* /root/autodl-tmp/sft_output*4B* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_output*4b* /root/autodl-tmp/sft_output*4B* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T07:33:25.907542+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:33:25.907695+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -maxdepth 2 -name \"adapter_config.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/ -maxdepth 2 -name \"adapter_config.json\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T07:33:25.907831+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:33:25.907980+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_output*4b* /root/autodl-tmp/sft_output*4B*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_output*4b* /root/autodl-tmp/sft_output*4B*",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T07:33:25.908106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -maxdepth 2 -name \"adapter_config.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/ -maxdepth 2 -name \"adapter_config.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T07:33:25.908264+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/autodl-tmp/sft_output_14b:\\ntotal 517408\\ndrwxr-xr-x  4 root root      4096 May 19 15:17 .\\ndrwxr-xr-x 82 root root      8192 May 21 03:17 ..\\n-rw-r--r--  1 root root      1470 May 19 15:17 README.md\\n-rw-r--r--  1 root root      1118 May 19 15:17 adapter_config.json\\n-rw-r--r--  1 root root 513878424 May 19 15:17 adapter_model.safetensors\\n-rw-r--r--  1 root root       707 May 19 15:17 added_tokens.json\\n-rw-r--r--  1 root root      4168 May 19 15:17 chat_template.jinja\\ndrwxr-xr-x  3 root root      4096 May 19 15:17 checkpoint-144\\ndrwxr-xr-x  3 root root      4096 May 19 14:17 checkpoint-96\\n-rw-r--r--  1 root root   1671853 May 19 15:17 merges.txt\\n-rw-r--r--  1 root root       499 May 19 15:17 special_tokens_map.json\\n-rw-r--r--  1 root root  11422654 May 19 15:17 tokenizer.json\\n-rw-r--r--  1 root root      5431 May 19 15:17 tokenizer_config.json\\n-rw-r--r--  1 root root      8337 May 19 15:17 training_args.bin\\n-rw-r--r--  1 root root   2776833 May 19 15:17 vocab.json\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/sft_output*4B*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T07:33:25.908460+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/grpo_bf16_g4/adapter_config.json\\n/root/autodl-tmp/rsft_output_4b_sft_s44/adapter_config.json\\n/root/autodl-tmp/rsft_output_4b_sft_s44_bf16/adapter_config.json\\n/root/autodl-tmp/rsft_output_ced_s43/adapter_config.json\\n/root/autodl-tmp/rsft_output_llama_3_1_8b_k1/adapter_config.json\\n/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43/adapter_config.json\\n/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44/adapter_config.json\\n/root/autodl-tmp/rsft_output_nli_large/adapter_config.json\\n/root/autodl-tmp/rsft_output_qwen3_1_7b_k1/adapter_config.json\\n/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43/adapter_config.json\\n/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44/adapter_config.json\\n/root/autodl-tmp/rsft_output_qwen3_8b_k1/adapter_config.json\\n/root/autodl-tmp/rsft_output_qwen3_8b_k1_s43/adapter_config.json\\n/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44/adapter_config.json\\n/root/autodl-tmp/rsft_output_random_k1/adapter_config.json\\n/root/autodl-tmp/sft_no_evidence_output/adapter_config.json\\n/root/autodl-tmp/sft_output/adapter_config.json\\n/root/autodl-tmp/sft_output_14b/adapter_config.json\\n/root/autodl-tmp/sft_output_llama_3_1_8b/adapter_config.json\\n/root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence/adapter_config.json\\n/root/autodl-tmp/sft_output_llama_3_1_8b_s43/adapter_config.json\\n/root/autodl-tmp/sft_output_llama_3_1_8b_s44/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed44/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_8b_bf16/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_8b_no_evidence/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_8b_s43/adapter_config.json\\n/root/autodl-tmp/sft_output_qwen3_8b_s44/adapter_con
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T07:33:25.908640+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/sft_output/adapter_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/sft_output/adapter_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T07:33:25.908766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/sft_output_seed43/adapter_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/sft_output_seed43/adapter_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T07:33:25.908887+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/sft_no_evidence_output/adapter_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/sft_no_evidence_output/adapter_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T07:33:25.909053+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 128,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.0\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 64,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"v_proj\\\",\\n    \\\"gate_proj\\\",\\n    \\\"q_proj\\\",\\n    \\\"o_proj\\\",\\n    \\\"down_proj\\\",\\n    \\\"up_proj\\\",\\n    \\\"k_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T07:33:25.909250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 128,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.0\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 64,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"o_proj\\\",\\n    \\\"k_proj\\\",\\n    \\\"down_proj\\\",\\n    \\\"q_proj\\\",\\n    \\\"gate_proj\\\",\\n    \\\"up_proj\\\",\\n    \\\"v_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T07:33:25.909434+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 128,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.0\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 64,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"o_proj\\\",\\n    \\\"v_proj\\\",\\n    \\\"down_proj\\\",\\n    \\\"q_proj\\\",\\n    \\\"gate_proj\\\",\\n    \\\"k_proj\\\",\\n    \\\"up_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T07:33:25.909613+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -50 /root/autodl-tmp/sft_output/trainer_state.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -50 /root/autodl-tmp/sft_output/trainer_state.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T07:33:25.909739+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -50 /root/autodl-tmp/sft_no_evidence_output/trainer_state.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -50 /root/autodl-tmp/sft_no_evidence_output/trainer_state.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T07:33:25.909863+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/autodl-tmp/sft_output/trainer_state.json' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T07:33:25.909985+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/autodl-tmp/sft_no_evidence_output/trainer_state.json' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T07:33:25.910135+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/sft_output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/sft_output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T07:33:25.910283+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nadded_tokens.json\\nchat_template.jinja\\ncheckpoint-144\\ncheckpoint-96\\nmerges.txt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T07:33:25.910411+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/sft_output/ -name \"trainer_state.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/sft_output/ -name \"trainer_state.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T07:33:25.910534+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/sft_output/checkpoint-144/trainer_state.json\\n/root/autodl-tmp/sft_output/checkpoint-96/trainer_state.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T07:33:25.910649+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -30 /root/autodl-tmp/sft_output/checkpoint-144/trainer_state.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -30 /root/autodl-tmp/sft_output/checkpoint-144/trainer_state.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T07:33:25.911158+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"best_global_step\\\": 144,\\n  \\\"best_metric\\\": 0.7200767397880554,\\n  \\\"best_model_checkpoint\\\": \\\"/root/autodl-tmp/sft_output/checkpoint-144\\\",\\n  \\\"epoch\\\": 3.0,\\n  \\\"eval_steps\\\": 500,\\n  \\\"global_step\\\": 144,\\n  \\\"is_hyper_param_search\\\": false,\\n  \\\"is_local_process_zero\\\": true,\\n  \\\"is_world_process_zero\\\": true,\\n  \\\"log_history\\\": [\\n    {\\n      \\\"entropy\\\": 0.9244873046875,\\n      \\\"epoch\\\": 0.21136063408190225,\\n      \\\"grad_norm\\\": 0.0792296901345253,\\n      \\\"learning_rate\\\": 0.0001985294117647059,\\n      \\\"loss\\\": 1.2741,\\n      \\\"mean_token_accuracy\\\": 0.7591710906475783,\\n      \\\"num_tokens\\\": 555730.0,\\n      \\\"step\\\": 10\\n    },\\n    {\\n      \\\"entropy\\\": 0.848193359375,\\n      \\\"epoch\\\": 0.4227212681638045,\\n      \\\"grad_norm\\\": 0.04085889458656311,\\n      \\\"learning_rate\\\": 0.0001838235294117647,\\n      \\\"loss\\\": 0.7883,\\n      \\\"mean_token_accuracy\\\": 0.8194206487387419,\\n      \\\"num_tokens\\\": 1106502.0,\\n      \\\"step\\\": 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T07:33:25.911404+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/sft_no_evidence_output/ -name \"trainer_state.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/sft_no_evidence_output/ -name \"trainer_state.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T07:33:25.911538+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/sft_no_evidence_output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/sft_no_evidence_output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T07:33:25.911667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/sft_no_evidence_output/checkpoint-190/trainer_state.json\\n/root/autodl-tmp/sft_no_evidence_output/checkpoint-570/trainer_state.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T07:33:25.911804+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nadded_tokens.json\\nchat_template.jinja\\ncheckpoint-190\\ncheckpoint-570\\nmerges.txt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T07:33:25.911929+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/sft_output_qwen3_8b_bf16/ -name \"trainer_state.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/sft_output_qwen3_8b_bf16/ -name \"trainer_state.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T07:33:25.912050+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16/checkpoint-190/trainer_state.json\\n/root/autodl-tmp/sft_output_qwen3_8b_bf16/checkpoint-570/trainer_state.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T07:33:25.912209+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -30 /root/autodl-tmp/sft_output_qwen3_8b_bf16/checkpoint-570/trainer_state.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -30 /root/autodl-tmp/sft_output_qwen3_8b_bf16/checkpoint-570/trainer_state.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T07:33:25.912384+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"best_global_step\\\": 190,\\n  \\\"best_metric\\\": 0.6813984513282776,\\n  \\\"best_model_checkpoint\\\": \\\"/root/autodl-tmp/sft_output_qwen3_8b_bf16/checkpoint-190\\\",\\n  \\\"epoch\\\": 3.0,\\n  \\\"eval_steps\\\": 500,\\n  \\\"global_step\\\": 570,\\n  \\\"is_hyper_param_search\\\": false,\\n  \\\"is_local_process_zero\\\": true,\\n  \\\"is_world_process_zero\\\": true,\\n  \\\"log_history\\\": [\\n    {\\n      \\\"entropy\\\": 0.6421456978656351,\\n      \\\"epoch\\\": 0.052857614800132145,\\n      \\\"grad_norm\\\": 0.4840833842754364,\\n      \\\"learning_rate\\\": 6.206896551724138e-05,\\n      \\\"loss\\\": 1.248,\\n      \\\"mean_token_accuracy\\\": 0.7474235128611326,\\n      \\\"num_tokens\\\": 141227.0,\\n      \\\"step\\\": 10\\n    },\\n    {\\n      \\\"entropy\\\": 0.9501719243824482,\\n      \\\"epoch\\\": 0.10571522960026429,\\n      \\\"grad_norm\\\": 0.20185545086860657,\\n      \\\"learning_rate\\\": 0.00013103448275862068,\\n      \\\"loss\\\": 0.8207,\\n      \\\"mean_token_accuracy\\\": 0.8024970300495624,\\n      \\\"num_tokens\\\": 276962.0,\\n      \\\"step\\\": 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T07:33:25.912534+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -30 /root/autodl-tmp/sft_output_qwen3_1_7b_bf16/checkpoint-570/trainer_state.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -30 /root/autodl-tmp/sft_output_qwen3_1_7b_bf16/checkpoint-570/trainer_state.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T07:33:25.912683+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"best_global_step\\\": 380,\\n  \\\"best_metric\\\": 0.7873569130897522,\\n  \\\"best_model_checkpoint\\\": \\\"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/checkpoint-380\\\",\\n  \\\"epoch\\\": 3.0,\\n  \\\"eval_steps\\\": 500,\\n  \\\"global_step\\\": 570,\\n  \\\"is_hyper_param_search\\\": false,\\n  \\\"is_local_process_zero\\\": true,\\n  \\\"is_world_process_zero\\\": true,\\n  \\\"log_history\\\": [\\n    {\\n      \\\"entropy\\\": 0.7330757294781506,\\n      \\\"epoch\\\": 0.052857614800132145,\\n      \\\"grad_norm\\\": 0.8391917943954468,\\n      \\\"learning_rate\\\": 6.206896551724138e-05,\\n      \\\"loss\\\": 1.5694,\\n      \\\"mean_token_accuracy\\\": 0.716822512820363,\\n      \\\"num_tokens\\\": 141227.0,\\n      \\\"step\\\": 10\\n    },\\n    {\\n      \\\"entropy\\\": 1.0906264197081328,\\n      \\\"epoch\\\": 0.10571522960026429,\\n      \\\"grad_norm\\\": 0.3718288838863373,\\n      \\\"learning_rate\\\": 0.00013103448275862068,\\n      \\\"loss\\\": 0.958,\\n      \\\"mean_token_accuracy\\\": 0.7808495718985796,\\n      \\\"num_tokens\\\": 276962.0,\\n      \\\"step\\\": 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T07:33:25.912814+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/sft_output_qwen3_1_7b_bf16/ -name \"trainer_state.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/sft_output_qwen3_1_7b_bf16/ -name \"trainer_state.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T07:33:25.912936+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/checkpoint-380/trainer_state.json\\n/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/checkpoint-570/trainer_state.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T07:33:25.913109+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -30 /root/autodl-tmp/sft_no_evidence_output/checkpoint-570/trainer_state.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -30 /root/autodl-tmp/sft_no_evidence_output/checkpoint-570/trainer_state.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T07:33:25.913313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"best_global_step\\\": 190,\\n  \\\"best_metric\\\": 0.8374003171920776,\\n  \\\"best_model_checkpoint\\\": \\\"/root/autodl-tmp/sft_no_evidence_output/checkpoint-190\\\",\\n  \\\"epoch\\\": 3.0,\\n  \\\"eval_steps\\\": 500,\\n  \\\"global_step\\\": 570,\\n  \\\"is_hyper_param_search\\\": false,\\n  \\\"is_local_process_zero\\\": true,\\n  \\\"is_world_process_zero\\\": true,\\n  \\\"log_history\\\": [\\n    {\\n      \\\"entropy\\\": 0.8077931884676218,\\n      \\\"epoch\\\": 0.052857614800132145,\\n      \\\"grad_norm\\\": 0.73046875,\\n      \\\"learning_rate\\\": 6.206896551724138e-05,\\n      \\\"loss\\\": 1.5467,\\n      \\\"mean_token_accuracy\\\": 0.7150686398148537,\\n      \\\"num_tokens\\\": 119651.0,\\n      \\\"step\\\": 10\\n    },\\n    {\\n      \\\"entropy\\\": 1.08616476431489,\\n      \\\"epoch\\\": 0.10571522960026429,\\n      \\\"grad_norm\\\": 0.3125,\\n      \\\"learning_rate\\\": 0.00013103448275862068,\\n      \\\"loss\\\": 0.9787,\\n      \\\"mean_token_accuracy\\\": 0.7783265620470047,\\n      \\\"num_tokens\\\": 235585.0,\\n      \\\"step\\\": 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T07:33:25.913559+00:00_

Confirmed.

| Adapter | num_tokens @ step 10 | Total steps | Total tokens (~) |
|---|---|---|---|
| `sft_output_qwen3_8b_bf16` (standard 8B) | **141,227** | 570 | ~8.05M |
| `sft_output_qwen3_1_7b_bf16` (standard 1.7B) | **141,227** | 570 | ~8.05M |
| **`sft_output`** (Qwen3-4B candidate) | 555,730 | 144 | **~8.00M** |
| `sft_no_evidence_output` (no-evidence 4B) | **119,651** | 570 | ~6.82M |

**结论：`/root/autodl-tmp/sft_output/` 是 Qwen3-4B 的标准 SFT adapter（含 evidence）。**

- `base_model_name_or_path` = `/root/autodl-tmp/models/Qwen3-4B`
- 总训练 token 数 ~8.0M，与 8B/1.7B 标准 SFT (~8.05M) 一致
- no-evidence 版本 (`sft_no_evidence_output`) 仅 ~6.82M tokens（少了 evidence 字段的 token），与预期匹配
- 该 adapter 使用了更大 batch size（~4x），因此 steps 少（144 vs 570）但每步 token 多，总数据量一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_find-4b-sft-adapter_20260521T073041"
}
```

</details>

---
