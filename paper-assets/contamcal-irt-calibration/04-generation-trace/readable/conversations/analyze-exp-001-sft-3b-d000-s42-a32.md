# analyze exp 001 sft 3B d000 s42 a32

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718.jsonl`
- **Structured JSON:** [`4620be9d804412f26112.json`](../../sessions/46/4620be9d804412f26112.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-16T00:08:49.340270+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:08:49.344978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "ToolSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:08:49.345339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T00:08:49.345586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T00:08:49.349891+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.133, 'grad_norm': 0.2729591131210327, 'learning_rate': 1.152042759996232e-05, 'entropy': 1.1188414855860174, 'num_tokens': 13611325.0, 'mean_token_accuracy': 0.7495825739577413, 'epoch': 0.7}\\n{'loss': 1.1569, 'grad_norm': 0.28617748618125916, 'learning_rate': 1.1298325201076718e-05, 'entropy': 1.1255229650065304, 'num_tokens': 13671165.0, 'mean_token_accuracy': 0.7446877717971802, 'epoch': 0.7}\\n{'loss': 1.2498, 'grad_norm': 0.2639084756374359, 'learning_rate': 1.1077757919444825e-05, 'entropy': 1.200976430531591, 'num_tokens': 13734267.0, 'mean_token_accuracy': 0.7381640776991845, 'epoch': 0.7}\\n{'loss': 1.179, 'grad_norm': 0.1940835565328598, 'learning_rate': 1.0858750467128833e-05, 'entropy': 1.1109736337326468, 'num_tokens': 13798330.0, 'mean_token_accuracy': 0.743584344163537, 'epoch': 0.71}\\n{'loss': 1.0937, 'grad_norm': 0.23342503607273102, 'learning_rate': 1.0641327381429722e-05, 'entropy': 1.1195867702364921, 'num_tokens': 13857896.0, 'mean_token_accuracy': 0.745890948921442, 'epoch': 0.71}\\n{'loss': 1.0969, 'grad_norm': 0.25516387820243835, 'learning_rate': 1.0425513022138203e-05, 'entropy': 1.040596268698573, 'num_tokens': 13921550.0, 'mean_token_accuracy': 0.763890047557652, 'epoch': 0.71}\\n{'loss': 1.0488, 'grad_norm': 0.2416841834783554, 'learning_rate': 1.0211331568805399e-05, 'entropy': 1.116150265466422, 'num_tokens': 13988306.0, 'mean_token_accuracy': 0.7439524015411735, 'epoch': 0.72}\\n{'loss': 1.0759, 'grad_norm': 0.23474155366420746, 'learning_rate': 9.998807018033871e-06, 'entropy': 1.0970942040905356, 'num_tokens': 14047116.0, 'mean_token_accuracy': 0.7535396873950958, 'epoch': 0.72}\\n{'loss': 1.0647, 'grad_norm': 0.458779513835907, 'learning_rate': 9.787963180789039e-06, 'entropy': 1.0978553163819016, 'num_tokens': 14110302.0, 'mean_token_accuracy': 0.7500880684703588, 'epoch': 0.72}\\n{'loss': 1.1182, 'grad_norm': 0.4449751675128937, 'learning_rate': 9.57882367973141
…[truncated 6282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T00:08:49.350215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  3 root root   63 May 14 07:20 .\\ndrwxr-xr-x 34 root root 4096 May 16 04:12 ..\\ndrwxr-xr-x  3 root root 4096 May 14 07:20 lora_adapter\\n-rw-r--r--  1 root root  305 May 16 08:03 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T00:08:49.352619+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:08:49.352888+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 132544\\ndrwxr-xr-x 3 root root      4096 May 14 07:20 .\\ndrwxr-xr-x 3 root root        63 May 14 07:20 ..\\n-rw-r--r-- 1 root root      1468 May 16 08:03 README.md\\n-rw-r--r-- 1 root root      1121 May 16 08:03 adapter_config.json\\n-rw-r--r-- 1 root root 119801528 May 16 08:03 adapter_model.safetensors\\n-rw-r--r-- 1 root root       605 May 16 08:03 added_tokens.json\\n-rw-r--r-- 1 root root      2427 May 16 08:03 chat_template.jinja\\ndrwxr-xr-x 2 root root      4096 May 14 07:20 checkpoint-3125\\n-rw-r--r-- 1 root root   1671853 May 16 08:03 merges.txt\\n-rw-r--r-- 1 root root       502 May 16 08:03 special_tokens_map.json\\n-rw-r--r-- 1 root root  11421896 May 16 08:03 tokenizer.json\\n-rw-r--r-- 1 root root      4689 May 16 08:03 tokenizer_config.json\\n-rw-r--r-- 1 root root      6417 May 16 08:03 training_args.bin\\n-rw-r--r-- 1 root root   2776833 May 16 08:03 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:08:49.353106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:08:49.353380+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 32,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.0\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 16,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"down_proj\\\",\\n    \\\"o_proj\\\",\\n    \\\"k_proj\\\",\\n    \\\"q_proj\\\",\\n    \\\"gate_proj\\\",\\n    \\\"v_proj\\\",\\n    \\\"up_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:08:49.353718+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:08:49.355651+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:02.257Z\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8933}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:08:49.355883+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "metrics",
  "value": "{'final_loss': 1.1324, 'total_steps': 3125, 'training_time_sec': 12647.38, 'train_samples_per_second': 3.953, 'mean_token_accuracy': 0.7333, 'entropy': 1.1654}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "metrics",
    "value": "{'final_loss': 1.1324, 'total_steps': 3125, 'training_time_sec': 12647.38, 'train_samples_per_second': 3.953, 'mean_token_accuracy': 0.7333, 'entropy': 1.1654}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:08:49.356124+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:03.702Z\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1324, \"total_steps\": 3125, \"training_time_sec\": 12647.38, \"train_samples_per_second\": 3.953, \"mean_token_accuracy\": 0.7333, \"entropy\": 1.1654}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7906}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:08:49.356348+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:08:49.356571+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:05.120Z\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1324, \"total_steps\": 3125, \"training_time_sec\": 12647.38, \"train_samples_per_second\": 3.953, \"mean_token_accuracy\": 0.7333, \"entropy\": 1.1654}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8025}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:08:49.356790+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "log_path",
  "value": "~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "log_path",
    "value": "~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:08:49.357012+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:06.276Z\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1324, \"total_steps\": 3125, \"training_time_sec\": 12647.38, \"train_samples_per_second\": 3.953, \"mean_token_accuracy\": 0.7333, \"entropy\": 1.1654}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7725}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:08:49.357215+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:08:49.361653+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.474}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T00:08:49.362024+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl', 'data_count': 50000, 'model_name': 'Qwen2.5-3B', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl', 'data_count': 50000, 'model_name': 'Qwen2.5-3B', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T00:08:49.362281+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3827}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:08:49.362503+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T00:08:49.362720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:25.567Z\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1324, \"total_steps\": 3125, \"training_time_sec\": 12647.38, \"train_samples_per_second\": 3.953, \"mean_token_accuracy\": 0.7333, \"entropy\": 1.1654}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1731}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T00:08:49.362948+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl', 'data_count': 50000, 'model_name': 'Qwen2.5-3B', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl', 'data_count': 50000, 'model_name': 'Qwen2.5-3B', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T00:08:49.363193+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:33.159Z\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1324, \"total_steps\": 3125, \"training_time_sec\": 12647.38, \"train_samples_per_second\": 3.953, \"mean_token_accuracy\": 0.7333, \"entropy\": 1.1654}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0223}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T00:08:49.365510+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_3B_d000_s42_a32",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_3B_d000_s42_a32",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T00:08:49.365812+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_3B_d000_s42_a32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:02.257Z\", \"updated_at\": \"2026-05-16T00:08:37.600Z\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1324, \"total_steps\": 3125, \"training_time_sec\": 12647.38, \"train_samples_per_second\": 3.953, \"mean_token_accuracy\": 0.7333, \"entropy\": 1.1654}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42}, \"completed_at\": \"2026-05-16T00:08:37.600Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0538}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-16T00:08:49.366134+00:00_

Registry 已更新为 DONE/success。

## 实验结果摘要

| 项目 | 值 |
|------|-----|
| **状态** | 训练成功完成 (EXIT_CODE=0) |
| **Final loss** | 1.1324 |
| **总步数** | 3,125 steps |
| **训练时间** | 12,647s (~3h 31min) |
| **Mean token accuracy** | 0.7333 |
| **Checkpoint 路径** | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/` |

**Checkpoint 文件**:
- `adapter_model.safetensors` (114MB)
- `adapter_config.json` — 确认 **lora_alpha=32**, r=16, target_modules=[q/k/v/o/gate/up/down_proj]
- tokenizer 文件完整

**adapter_config 关键参数**: lora_alpha=32, r=16, dropout=0.05, bias=none, task=CAUSAL_LM, base_model=Qwen2.5-3B

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718"
}
```

</details>

---
