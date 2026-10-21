# analysis exp 001 sft 3B d100 s42 a32 v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149.jsonl`
- **Structured JSON:** [`4d257cc5218aec077040.json`](../../sessions/4d/4d257cc5218aec077040.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-16T01:12:43.759946+00:00_

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
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
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

_source line 2 · 2026-05-16T01:12:43.762533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:12:43.762905+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T01:12:43.763163+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T01:12:43.763404+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T01:12:43.763719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.1747, 'grad_norm': 0.19925163686275482, 'learning_rate': 6.799751784942232e-06, 'entropy': 1.2200136814266442, 'num_tokens': 16711209.0, 'mean_token_accuracy': 0.7297933172434569, 'epoch': 0.77}\\n{'loss': 1.283, 'grad_norm': 0.4196663796901703, 'learning_rate': 6.664048453314822e-06, 'entropy': 1.2995388239622117, 'num_tokens': 16762695.0, 'mean_token_accuracy': 0.7150606691837311, 'epoch': 0.77}\\n{'loss': 1.1394, 'grad_norm': 0.2641744315624237, 'learning_rate': 6.529504397702254e-06, 'entropy': 1.2233203757554292, 'num_tokens': 16814736.0, 'mean_token_accuracy': 0.7319713745266199, 'epoch': 0.78}\\n{'loss': 1.18, 'grad_norm': 0.30292075872421265, 'learning_rate': 6.396128124545886e-06, 'entropy': 1.2152106568217278, 'num_tokens': 16868568.0, 'mean_token_accuracy': 0.730739694647491, 'epoch': 0.78}\\n{'loss': 1.1575, 'grad_norm': 0.3119448125362396, 'learning_rate': 6.26392806645496e-06, 'entropy': 1.257698342204094, 'num_tokens': 16923622.0, 'mean_token_accuracy': 0.7243348453193903, 'epoch': 0.78}\\n{'loss': 1.1498, 'grad_norm': 0.3739565312862396, 'learning_rate': 6.1329125816734555e-06, 'entropy': 1.2718367166817188, 'num_tokens': 16977459.0, 'mean_token_accuracy': 0.7248291462659836, 'epoch': 0.78}\\n{'loss': 1.1313, 'grad_norm': 0.43050241470336914, 'learning_rate': 6.003089953551632e-06, 'entropy': 1.248955331556499, 'num_tokens': 17027823.0, 'mean_token_accuracy': 0.7324004296213389, 'epoch': 0.79}\\n{'loss': 1.3173, 'grad_norm': 0.28954198956489563, 'learning_rate': 5.8744683900223305e-06, 'entropy': 1.3010762742720545, 'num_tokens': 17085291.0, 'mean_token_accuracy': 0.713843691907823, 'epoch': 0.79}\\n{'loss': 1.0794, 'grad_norm': 0.23684027791023254, 'learning_rate': 5.747056023082043e-06, 'entropy': 1.2058127548545599, 'num_tokens': 17136589.0, 'mean_token_accuracy': 0.734391955845058, 'epoch': 0.79}\\n{'loss': 1.1246, 'grad_norm': 0.3383660614490509, 'learning_rate': 5.62086090827676
…[truncated 6282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T01:12:43.763973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  3 root root   63 May 16 09:07 .\\ndrwxr-xr-x 33 root root 4096 May 16 09:10 ..\\ndrwxr-xr-x  3 root root 4096 May 16 09:07 lora_adapter\\n-rw-r--r--  1 root root  305 May 16 09:07 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:12:43.764211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 132544\\ndrwxr-xr-x 3 root root      4096 May 16 09:07 .\\ndrwxr-xr-x 3 root root        63 May 16 09:07 ..\\n-rw-r--r-- 1 root root      1468 May 16 09:07 README.md\\n-rw-r--r-- 1 root root      1121 May 16 09:07 adapter_config.json\\n-rw-r--r-- 1 root root 119801528 May 16 09:07 adapter_model.safetensors\\n-rw-r--r-- 1 root root       605 May 16 09:07 added_tokens.json\\n-rw-r--r-- 1 root root      2427 May 16 09:07 chat_template.jinja\\ndrwxr-xr-x 2 root root      4096 May 16 09:07 checkpoint-4159\\n-rw-r--r-- 1 root root   1671853 May 16 09:07 merges.txt\\n-rw-r--r-- 1 root root       502 May 16 09:07 special_tokens_map.json\\n-rw-r--r-- 1 root root  11421896 May 16 09:07 tokenizer.json\\n-rw-r--r-- 1 root root      4689 May 16 09:07 tokenizer_config.json\\n-rw-r--r-- 1 root root      6417 May 16 09:07 training_args.bin\\n-rw-r--r-- 1 root root   2776833 May 16 09:07 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T01:12:43.768630+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -i wandb ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -i wandb ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T01:12:43.768915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T01:12:43.769127+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T01:12:43.769394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 32,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.0\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 16,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"up_proj\\\",\\n    \\\"o_proj\\\",\\n    \\\"down_proj\\\",\\n    \\\"v_proj\\\",\\n    \\\"gate_proj\\\",\\n    \\\"q_proj\\\",\\n    \\\"k_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T01:12:43.769728+00:00_

训练正常完成，checkpoint 完整。

```
STATUS: success
CHECKPOINT_PATH: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter
LOG_PATH: ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log
FINAL_LOSS: 1.1795 (train_loss avg)
TOTAL_STEPS: 4159
TRAINING_TIME: 294 min (4h 54m)
WANDB_RUN_ID: N/A (no W&B logging detected)
NOTES:
- EXIT_CODE=0, epoch=1.0, cosine LR schedule fully decayed
- adapter_model.safetensors = 114.2 MB ✓
- lora_alpha=32, r=16 confirmed ✓
- mean_token_accuracy: 0.7186
- 3.771 samples/sec, 0.236 steps/sec
- Last-step loss ~1.19-1.21, consistent with avg — no divergence
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149"
}
```

</details>

---
