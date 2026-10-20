# analyze exp 001 sft phi4 d005 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309.jsonl`
- **Structured JSON:** [`a6b8d16a1d32ae882523.json`](../../sessions/a6/a6b8d16a1d32ae882523.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-19T03:24:19.880031+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T03:24:19.880510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:24:19.880725+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_sft_phi4_d005_s42'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_sft_phi4_d005_s42'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T03:24:19.880870+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "tail -50 ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "tail -50 ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T03:24:19.881011+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7437}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T03:24:19.881141+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/train_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/train_config.json"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:24:19.881268+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/.done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/.done"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:24:19.881666+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 86%|████████▌ | 2720/3177 [2:13:09<22:41,  2.98s/it]\\r 86%|████████▌ | 2721/3177 [2:13:12<21:40,  2.85s/it]\\r 86%|████████▌ | 2722/3177 [2:13:15<22:28,  2.96s/it]\\r 86%|████████▌ | 2723/3177 [2:13:18<21:36,  2.86s/it]\\r 86%|████████▌ | 2724/3177 [2:13:20<20:37,  2.73s/it]\\r 86%|████████▌ | 2725/3177 [2:13:23<21:11,  2.81s/it]\\r 86%|████████▌ | 2726/3177 [2:13:27<23:26,  3.12s/it]\\r 86%|████████▌ | 2727/3177 [2:13:30<22:42,  3.03s/it]\\r 86%|████████▌ | 2728/3177 [2:13:32<21:32,  2.88s/it]\\r 86%|████████▌ | 2729/3177 [2:13:35<21:49,  2.92s/it]\\r 86%|████████▌ | 2730/3177 [2:13:39<22:40,  3.04s/it]\\r                                                     \\r{'loss': '1.144', 'grad_norm': '0.3845', 'learning_rate': '2.67e-06', 'entropy': '1.054', 'num_tokens': '1.656e+07', 'mean_token_accuracy': '0.7391', 'epoch': '0.8594'}\\n\\r 86%|████████▌ | 2730/3177 [2:13:39<22:40,  3.04s/it]\\r 86%|████████▌ | 2731/3177 [2:13:42<22:07,  2.98s/it]\\r 86%|████████▌ | 2732/3177 [2:13:45<23:00,  3.10s/it]\\r 86%|████████▌ | 2733/3177 [2:13:47<21:12,  2.87s/it]\\r 86%|████████▌ | 2734/3177 [2:13:50<21:10,  2.87s/it]\\r 86%|████████▌ | 2735/3177 [2:13:53<21:09,  2.87s/it]\\r 86%|████████▌ | 2736/3177 [2:13:56<20:51,  2.84s/it]\\r 86%|████████▌ | 2737/3177 [2:13:59<21:49,  2.98s/it]\\r 86%|████████▌ | 2738/3177 [2:14:02<21:20,  2.92s/it]\\r 86%|████████▌ | 2739/3177 [2:14:04<20:25,  2.80s/it]\\r 86%|████████▌ | 2740/3177 [2:14:07<20:08,  2.77s/it]\\r                                                     \\r{'loss': '1.047', 'grad_norm': '0.4362', 'learning_rate': '2.554e-06', 'entropy': '1.021', 'num_tokens': '1.662e+07', 'mean_token_accuracy': '0.7514', 'epoch': '0.8626'}\\n\\r 86%|████████▌ | 2740/3177 [2:14:07<20:08,  2.77s/it]\\r 86%|████████▋ | 2741/3177 [2:14:10<21:28,  2.96s/it]\\r 86%|████████▋ | 2742/3177 [2:14:13<21:10,  2.92s/it]\\r 86%|████████▋ | 2743/3177 [2:14:16<21:42,  3.00s/it]\\r 86%|████████▋ | 2744/31
…[truncated 6472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:24:19.881941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:24:19.882135+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"/root/autodl-tmp/models/phi-4\\\",\\n  \\\"data_path\\\": \\\"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\\\",\\n  \\\"lora_r\\\": 16,\\n  \\\"lora_alpha\\\": 32,\\n  \\\"epochs\\\": 1,\\n  \\\"batch_size\\\": 1,\\n  \\\"grad_accum\\\": 16,\\n  \\\"lr\\\": 5e-05,\\n  \\\"max_seq_length\\\": 2048,\\n  \\\"seed\\\": 42,\\n  \\\"num_samples\\\": 50826,\\n  \\\"gradient_checkpointing\\\": false,\\n  \\\"load_in_4bit\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T03:24:19.882348+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 5 May 19 11:18 /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42/.done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:24:19.882512+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 224664\\ndrwxr-xr-x 3 root root      4096 May 19 11:18 .\\ndrwxr-xr-x 3 root root        80 May 19 11:18 ..\\n-rw-r--r-- 1 root root      1446 May 19 11:18 README.md\\n-rw-r--r-- 1 root root      1070 May 19 11:18 adapter_config.json\\n-rw-r--r-- 1 root root 222865880 May 19 11:18 adapter_model.safetensors\\n-rw-r--r-- 1 root root       462 May 19 11:18 chat_template.jinja\\ndrwxr-xr-x 2 root root      4096 May 19 11:18 checkpoint-3177\\n-rw-r--r-- 1 root root   7153464 May 19 11:18 tokenizer.json\\n-rw-r--r-- 1 root root       312 May 19 11:18 tokenizer_config.json\\n-rw-r--r-- 1 root root      5777 May 19 11:18 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:24:19.882720+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "grep -i \"wandb\" ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "grep -i \"wandb\" ~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:24:19.882876+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:24:19.883012+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "fields": "['*']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "fields": "['*']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:24:19.883472+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_sft_phi4_d005_s42\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:20:46.363Z\", \"updated_at\": \"2026-05-19T03:20:49.709Z\", \"hypothesis\": \"Phi-4 (14.7B) d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dosage chain with dual-GPU acceleration (d005 on cuda:3 while d000 runs on cuda:2).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"90908\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:20:47.256Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:20:57.739969+00:00\"}]}}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:42:21.230Z\", \"updated_at\": \"2026-05-19T03:13:23.897Z\", \"hypothesis\": \"OLMo-2-7B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the AllenAI model family, running in parallel 
…[truncated 20442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:24:19.884078+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_phi4_d005_s42",
  "field": "metrics",
  "value": "{'final_loss': 1.185, 'final_eval_accuracy': 0.7302, 'total_steps': 3177, 'train_runtime_seconds': 9321, 'wandb_run_id': None}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_phi4_d005_s42",
    "field": "metrics",
    "value": "{'final_loss': 1.185, 'final_eval_accuracy': 0.7302, 'total_steps': 3177, 'train_runtime_seconds': 9321, 'wandb_run_id': None}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T03:24:19.884284+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_phi4_d005_s42",
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
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_phi4_d005_s42",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T03:24:19.886670+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_phi4_d005_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:20:46.363Z\", \"updated_at\": \"2026-05-19T03:24:03.843Z\", \"hypothesis\": \"Phi-4 (14.7B) d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dosage chain with dual-GPU acceleration (d005 on cuda:3 while d000 runs on cuda:2).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"90908\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:20:47.256Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:20:57.739969+00:00\"}]}, \"metrics\": {\"final_loss\": 1.185, \"final_eval_accuracy\": 0.7302, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2754}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:24:19.887067+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_phi4_d005_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:20:46.363Z\", \"updated_at\": \"2026-05-19T03:24:05.173Z\", \"hypothesis\": \"Phi-4 (14.7B) d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dosage chain with dual-GPU acceleration (d005 on cuda:3 while d000 runs on cuda:2).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"90908\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:20:47.256Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:20:57.739969+00:00\"}]}, \"metrics\": {\"final_loss\": 1.185, \"final_eval_accuracy\": 0.7302, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3446}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:24:19.889474+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_phi4_d005_s42",
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
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_phi4_d005_s42",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:24:19.889914+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_phi4_d005_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:20:46.363Z\", \"updated_at\": \"2026-05-19T03:24:09.776Z\", \"hypothesis\": \"Phi-4 (14.7B) d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dosage chain with dual-GPU acceleration (d005 on cuda:3 while d000 runs on cuda:2).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"90908\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:20:47.256Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:20:57.739969+00:00\"}]}, \"metrics\": {\"final_loss\": 1.185, \"final_eval_accuracy\": 0.7302, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:24:09.776Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1763}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T03:24:19.890159+00:00_

## Phi-4 d005 SFT 分析摘要

| 指标 | d005 | d000 (baseline) | 差异 |
|------|------|-----------------|------|
| final_loss (avg) | 1.185 | 1.183 | +0.002 |
| mean_token_accuracy | 0.7302 | 0.7287 | +0.0015 |
| total_steps | 3177 | 3125 | +52 (数据量略多) |
| train_runtime | 9321s (~2h35m) | 7500s (~2h05m) | +1821s |
| W&B | 无 | - | - |

**结论：success。** 训练正常完成，`.done` sentinel 存在，adapter 文件完整（222MB safetensors + tokenizer + config）。Loss 和 accuracy 与 d000 几乎一致，符合 5% 低污染剂量的预期（污染比例太低，对训练损失无显著影响）。lora_alpha=32 确认合规。无 W&B 日志。

注册表已更新为 DONE/success，checkpoint_path 和 log_path 均已设置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309"
}
```

</details>

---
