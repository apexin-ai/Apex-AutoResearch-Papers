# analysis exp 001 sft phi4 d025 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343.jsonl`
- **Structured JSON:** [`9763f9b3b2771d4ed0a8.json`](../../sessions/97/9763f9b3b2771d4ed0a8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-19T03:55:18.523209+00:00_

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
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
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

_source line 2 · 2026-05-19T03:55:18.523698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:55:18.523974+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T03:55:18.524183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T03:55:18.524530+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 72%|███████▏  | 2430/3384 [1:35:12<38:03,  2.39s/it]\\r 72%|███████▏  | 2431/3384 [1:35:14<37:24,  2.35s/it]\\r 72%|███████▏  | 2432/3384 [1:35:17<36:38,  2.31s/it]\\r 72%|███████▏  | 2433/3384 [1:35:19<36:56,  2.33s/it]\\r 72%|███████▏  | 2434/3384 [1:35:21<36:48,  2.32s/it]\\r 72%|███████▏  | 2435/3384 [1:35:24<37:18,  2.36s/it]\\r 72%|███████▏  | 2436/3384 [1:35:26<38:30,  2.44s/it]\\r 72%|███████▏  | 2437/3384 [1:35:29<38:16,  2.42s/it]\\r 72%|███████▏  | 2438/3384 [1:35:31<37:35,  2.38s/it]\\r 72%|███████▏  | 2439/3384 [1:35:33<37:03,  2.35s/it]\\r 72%|███████▏  | 2440/3384 [1:35:36<37:06,  2.36s/it]\\r                                                     \\r{'loss': '1.116', 'grad_norm': '0.3478', 'learning_rate': '9.928e-06', 'entropy': '1.071', 'num_tokens': '1.413e+07', 'mean_token_accuracy': '0.7383', 'epoch': '0.7212'}\\n\\r 72%|███████▏  | 2440/3384 [1:35:36<37:06,  2.36s/it]\\r 72%|███████▏  | 2441/3384 [1:35:38<35:31,  2.26s/it]\\r 72%|███████▏  | 2442/3384 [1:35:40<36:20,  2.32s/it]\\r 72%|███████▏  | 2443/3384 [1:35:42<36:22,  2.32s/it]\\r 72%|███████▏  | 2444/3384 [1:35:45<39:10,  2.50s/it]\\r 72%|███████▏  | 2445/3384 [1:35:49<43:42,  2.79s/it]\\r 72%|███████▏  | 2446/3384 [1:35:51<40:49,  2.61s/it]\\r 72%|███████▏  | 2447/3384 [1:35:54<41:25,  2.65s/it]\\r 72%|███████▏  | 2448/3384 [1:35:56<41:38,  2.67s/it]\\r 72%|███████▏  | 2449/3384 [1:35:59<40:05,  2.57s/it]\\r 72%|███████▏  | 2450/3384 [1:36:01<39:15,  2.52s/it]\\r                                                     \\r{'loss': '1.172', 'grad_norm': '0.3001', 'learning_rate': '9.734e-06', 'entropy': '1.103', 'num_tokens': '1.419e+07', 'mean_token_accuracy': '0.7305', 'epoch': '0.7241'}\\n\\r 72%|█���█████▏  | 2450/3384 [1:36:01<39:15,  2.52s/it]\\r 72%|███████▏  | 2451/3384 [1:36:04<39:02,  2.51s/it]\\r 72%|███████▏  | 2452/3384 [1:36:06<38:04,  2.45s/it]\\r 72%|███████▏  | 2453/3384 [1:36:08<37:33,  2.42s/it]\\r 73%|███████▎  | 2454
…[truncated 6472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:55:18.524769+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  3 root root   80 May 19 11:49 .\\ndrwxr-xr-x 28 root root 4096 May 19 11:24 ..\\n-rw-r--r--  1 root root    5 May 19 11:49 .done\\ndrwxr-xr-x  3 root root 4096 May 19 11:49 lora_adapter\\n-rw-r--r--  1 root root  345 May 19 11:49 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:55:18.524964+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:55:18.525109+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 224664\\ndrwxr-xr-x 3 root root      4096 May 19 11:49 .\\ndrwxr-xr-x 3 root root        80 May 19 11:49 ..\\n-rw-r--r-- 1 root root      1446 May 19 11:49 README.md\\n-rw-r--r-- 1 root root      1070 May 19 11:49 adapter_config.json\\n-rw-r--r-- 1 root root 222865880 May 19 11:49 adapter_model.safetensors\\n-rw-r--r-- 1 root root       462 May 19 11:49 chat_template.jinja\\ndrwxr-xr-x 2 root root      4096 May 19 11:49 checkpoint-3384\\n-rw-r--r-- 1 root root   7153464 May 19 11:49 tokenizer.json\\n-rw-r--r-- 1 root root       312 May 19 11:49 tokenizer_config.json\\n-rw-r--r-- 1 root root      5777 May 19 11:49 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:55:18.525240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "grep -i \"wandb\" ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "grep -i \"wandb\" ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T03:55:18.525417+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "grep -i \"eval\" ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "grep -i \"eval\" ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T03:55:18.525555+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:55:18.525675+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:55:18.525822+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:55:18.525985+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alora_invocation_tokens\\\": null,\\n  \\\"alpha_pattern\\\": {},\\n  \\\"arrow_config\\\": null,\\n  \\\"auto_mapping\\\": null,\\n  \\\"base_model_name_or_path\\\": \\\"/root/autodl-tmp/models/phi-4\\\",\\n  \\\"bias\\\": \\\"none\\\",\\n  \\\"corda_config\\\": null,\\n  \\\"ensure_weight_tying\\\": false,\\n  \\\"eva_config\\\": null,\\n  \\\"exclude_modules\\\": null,\\n  \\\"fan_in_fan_out\\\": false,\\n  \\\"inference_mode\\\": true,\\n  \\\"init_lora_weights\\\": true,\\n  \\\"layer_replication\\\": null,\\n  \\\"layers_pattern\\\": null,\\n  \\\"layers_to_transform\\\": null,\\n  \\\"loftq_config\\\": {},\\n  \\\"lora_alpha\\\": 32,\\n  \\\"lora_bias\\\": false,\\n  \\\"lora_dropout\\\": 0.05,\\n  \\\"lora_ga_config\\\": null,\\n  \\\"megatron_config\\\": null,\\n  \\\"megatron_core\\\": \\\"megatron.core\\\",\\n  \\\"modules_to_save\\\": null,\\n  \\\"peft_type\\\": \\\"LORA\\\",\\n  \\\"peft_version\\\": \\\"0.19.1\\\",\\n  \\\"qalora_group_size\\\": 16,\\n  \\\"r\\\": 16,\\n  \\\"rank_pattern\\\": {},\\n  \\\"revision\\\": null,\\n  \\\"target_modules\\\": [\\n    \\\"gate_up_proj\\\",\\n    \\\"down_proj\\\",\\n    \\\"qkv_proj\\\",\\n    \\\"o_proj\\\"\\n  ],\\n  \\\"target_parameters\\\": null,\\n  \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n  \\\"trainable_token_indices\\\": null,\\n  \\\"use_bdlora\\\": null,\\n  \\\"use_dora\\\": false,\\n  \\\"use_qalora\\\": false,\\n  \\\"use_rslora\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:55:18.526175+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_phi4_d025_s42",
  "field": "metrics",
  "value": "{'train_loss': 1.187, 'mean_token_accuracy': 0.7527, 'total_steps': 3384, 'train_runtime_seconds': 7956, 'wandb_run_id': None, 'final_step_loss': 1.139, 'final_step_accuracy': 0.7329}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_phi4_d025_s42",
    "field": "metrics",
    "value": "{'train_loss': 1.187, 'mean_token_accuracy': 0.7527, 'total_steps': 3384, 'train_runtime_seconds': 7956, 'wandb_run_id': None, 'final_step_loss': 1.139, 'final_step_accuracy': 0.7329}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:55:18.526412+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_phi4_d025_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:45.934Z\", \"updated_at\": \"2026-05-19T03:54:53.939Z\", \"hypothesis\": \"Phi-4 (14.7B) d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dual-GPU dosage chain after d000 pilot success (loss=1.183, acc=0.729).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"93572\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:52:06.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:52:13.451411+00:00\"}]}, \"metrics\": {\"train_loss\": 1.187, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null, \"final_step_loss\": 1.139, \"final_step_accuracy\": 0.7329}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8644}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:55:18.526590+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_phi4_d025_s42",
  "field": "conclusion",
  "value": "success",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_phi4_d025_s42",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:55:18.526757+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_phi4_d025_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:45.934Z\", \"updated_at\": \"2026-05-19T03:54:58.503Z\", \"hypothesis\": \"Phi-4 (14.7B) d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dual-GPU dosage chain after d000 pilot success (loss=1.183, acc=0.729).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"93572\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:52:06.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:52:13.451411+00:00\"}]}, \"metrics\": {\"train_loss\": 1.187, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null, \"final_step_loss\": 1.139, \"final_step_accuracy\": 0.7329}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3416}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:55:18.526902+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_phi4_d025_s42",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_phi4_d025_s42",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:55:18.527092+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_phi4_d025_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:45.934Z\", \"updated_at\": \"2026-05-19T03:55:03.023Z\", \"hypothesis\": \"Phi-4 (14.7B) d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dual-GPU dosage chain after d000 pilot success (loss=1.183, acc=0.729).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"93572\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:52:06.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:52:13.451411+00:00\"}]}, \"metrics\": {\"train_loss\": 1.187, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null, \"final_step_loss\": 1.139, \"final_step_accuracy\": 0.7329}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:55:03.023Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_se
…[truncated 19 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T03:55:18.527293+00:00_

## 分析摘要

**exp_001_sft_phi4_d025_s42** 训练正常完成，已标记 DONE/success。

### 提取指标

| 指标 | 值 |
|---|---|
| train_loss (avg) | 1.187 |
| mean_token_accuracy (avg) | 0.7527 |
| final_step_loss (step 3380) | 1.139 |
| final_step_accuracy | 0.7329 |
| total_steps | 3384 |
| train_runtime | 7956s (2h13m) |
| W&B | 无 |
| checkpoint | 完整 (adapter_model.safetensors 213MB, lora_alpha=32 confirmed) |

### Dose-response 对比

| dosage | train_loss | acc |
|---|---|---|
| d000 (0%) | 1.183 | 0.7287 |
| d005 (5%) | 1.185 | 0.7302 |
| d025 (25%) | 1.187 | 0.7527 |

**趋势**：train_loss 三个 dosage 几乎持平（1.183→1.187），差异 <0.004，符合 null finding 预期。mean_token_accuracy d025 略高于 d000/d005（+0.02），可能因为 25% contamination 数据中 benchmark items 格式更规律、更易拟合，但需要后续 eval 阶段在 held-out benchmark 上验证这是否转化为实际性能差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343"
}
```

</details>

---
