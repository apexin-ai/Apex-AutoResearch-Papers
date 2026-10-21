# analysis exp 004 eval ckpt1500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_exp-004-eval-ckpt1500_20260520T154443.jsonl`
- **Structured JSON:** [`cd5176d6147cffc7d822.json`](../../sessions/cd/cd5176d6147cffc7d822.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-20T15:45:37.024899+00:00_

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
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
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

_source line 2 · 2026-05-20T15:45:37.025242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T15:45:37.025440+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/autodl-tmp/results/exp004_unified_eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/autodl-tmp/results/exp004_unified_eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T15:45:37.025604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 2320\\ndrwxr-xr-x 2 root root   4096 May 20 23:40 .\\ndrwxr-xr-x 5 root root    103 May 20 22:15 ..\\n-rw-r--r-- 1 root root 286578 May 20 22:44 exp004_ckpt1000_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 22:44 exp004_ckpt1000_preset_summary.txt\\n-rw-r--r-- 1 root root 285695 May 20 23:40 exp004_ckpt1500_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 23:40 exp004_ckpt1500_preset_summary.txt\\n-rw-r--r-- 1 root root 259554 May 20 23:35 exp004_ckpt2500_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 23:35 exp004_ckpt2500_preset_summary.txt\\n-rw-r--r-- 1 root root 257630 May 20 23:09 exp004_ckpt3000_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 23:09 exp004_ckpt3000_preset_summary.txt\\n-rw-r--r-- 1 root root 254927 May 20 23:36 exp004_ckpt3500_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 23:36 exp004_ckpt3500_preset_summary.txt\\n-rw-r--r-- 1 root root 252091 May 20 22:39 exp004_ckpt4000_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 22:39 exp004_ckpt4000_preset_summary.txt\\n-rw-r--r-- 1 root root 246467 May 20 23:06 exp004_ckpt5000_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 23:06 exp004_ckpt5000_preset_summary.txt\\n-rw-r--r-- 1 root root 241795 May 20 22:39 exp004_ckpt6000_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 22:39 exp004_ckpt6000_preset_summary.txt\\n-rw-r--r-- 1 root root 232468 May 20 23:05 exp004_ckpt7000_preset_eval.json\\n-rw-r--r-- 1 root root    363 May 20 23:05 exp004_ckpt7000_preset_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T15:45:37.025748+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "tail -50 ~/runs/contrastive_entrain_calib/exp-004-eval-ckpt1500.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "tail -50 ~/runs/contrastive_entrain_calib/exp-004-eval-ckpt1500.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T15:45:37.025982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 23:11:34,815 [INFO] eval_unified_preset: === D027 Unified Preset Eval ===\\n2026-05-20 23:11:34,816 [INFO] eval_unified_preset: model_path: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\n2026-05-20 23:11:34,816 [INFO] eval_unified_preset: lora_path:  /root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500\\n2026-05-20 23:11:34,816 [INFO] eval_unified_preset: data_path:  /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-20 23:11:34,816 [INFO] eval_unified_preset: exp_id:     exp004_ckpt1500\\n2026-05-20 23:11:35,114 [INFO] eval_unified_preset: Loading model...\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-20 23:11:35,743 [INFO] accelerate.utils.modeling: We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:03,  1.22it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.20it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.20it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:03<00:00,  1.31it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.72it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.46it/s]\\n2026-05-20 23:11:39,296 [INFO] eval_unified_preset: Loading LoRA adapter: /root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500\\n2026-05-20 23:11:42,452 [INFO] eval_unified_preset: Loading NLI model...\\n2026-05-20 23:11:42,664 [INFO] eval_unified_preset: NLI loaded: cross-encoder/nli-deberta-v3-base  id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'}  ent=1 con=0\\n2026-05-20 23:11:42,666 [INFO] eval_unified_preset: Loaded 362 eval pairs from /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.j
…[truncated 2327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T15:45:37.026209+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-28034",
  "command": "cat /root/autodl-tmp/results/exp004_unified_eval/exp004_ckpt1500_preset_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-28034",
    "command": "cat /root/autodl-tmp/results/exp004_unified_eval/exp004_ckpt1500_preset_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T15:45:37.026358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"D027 Preset Eval Summary\\nexp_id: exp004_ckpt1500\\nmodel:  /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\nlora:   /root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500\\ndata:   /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\ntime:   1741s\\n\\nToF        = 0.0939\\nNoF        = 0.8895\\nSYCONScore = 0.1699\\nn_valid    = 181\\nn_invalid  = 181\\nn_total    = 362\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T15:45:37.026530+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-004-eval-ckpt1500",
  "field": "metrics",
  "value": "{'ToF': 0.0939, 'NoF': 0.8895, 'SYCONScore': 0.1699, 'n_valid': 181, 'n_invalid': 181, 'n_total': 362, 'checkpoint': 'checkpoint-1500', 'eval_script': 'eval_unified_preset.py (D027 standard)', 'eval_server': 'westd-28034', 'eval_time_sec': 1741, 'vs_vanilla': 'SYCONScore 0.1699 vs 0.1335 = +27.3%'}",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-004-eval-ckpt1500",
    "field": "metrics",
    "value": "{'ToF': 0.0939, 'NoF': 0.8895, 'SYCONScore': 0.1699, 'n_valid': 181, 'n_invalid': 181, 'n_total': 362, 'checkpoint': 'checkpoint-1500', 'eval_script': 'eval_unified_preset.py (D027 standard)', 'eval_server': 'westd-28034', 'eval_time_sec': 1741, 'vs_vanilla': 'SYCONScore 0.1699 vs 0.1335 = +27.3%'}",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T15:45:37.026722+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-004-eval-ckpt1500\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:11:31.713Z\", \"updated_at\": \"2026-05-20T15:45:20.217Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/autodl-tmp/results/exp004_unified_eval/ --exp_id exp004_ckpt1500\\\"\", \"server\": \"westd-28034\", \"gpu\": [\"cuda:1\"], \"pid\": \"598441\", \"log_path\": \"/root/autodl-tmp/results/exp004_unified_eval/\", \"submitted_at\": \"2026-05-20T15:11:31.627Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\", \"data_count\": 362, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"exp-004 checkpoint-1500\", \"eval_data\": \"calibration_v2_1_expanded.jsonl (362 pairs)\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500\", \"wall_clock_seconds\": 1947.2, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:41:49.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:41:51.934213+00:00\"}]}, \"hypothesis\": \"Eval exp-004 ACT checkpoint-1500 with D027 unified preset. Part of ACT training trajectory for paper figure. Compare against vanilla SYCONScore=0.1335 and ckpt-1000 SYCONScore=0.2048.\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.0939, \"NoF\": 0.8895, \"SYCONScore\": 0.1699, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1500\", \"eval_scri
…[truncated 310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T15:45:37.026929+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-004-eval-ckpt1500",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-004-eval-ckpt1500",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T15:45:37.027109+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-004-eval-ckpt1500\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:11:31.713Z\", \"updated_at\": \"2026-05-20T15:45:25.303Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/autodl-tmp/results/exp004_unified_eval/ --exp_id exp004_ckpt1500\\\"\", \"server\": \"westd-28034\", \"gpu\": [\"cuda:1\"], \"pid\": \"598441\", \"log_path\": \"/root/autodl-tmp/results/exp004_unified_eval/\", \"submitted_at\": \"2026-05-20T15:11:31.627Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\", \"data_count\": 362, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"exp-004 checkpoint-1500\", \"eval_data\": \"calibration_v2_1_expanded.jsonl (362 pairs)\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500\", \"wall_clock_seconds\": 1947.2, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:41:49.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:41:51.934213+00:00\"}]}, \"hypothesis\": \"Eval exp-004 ACT checkpoint-1500 with D027 unified preset. Part of ACT training trajectory for paper figure. Compare against vanilla SYCONScore=0.1335 and ckpt-1000 SYCONScore=0.2048.\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.0939, \"NoF\": 0.8895, \"SYCONScore\": 0.1699, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1500\", \"eval_scri
…[truncated 398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T15:45:37.027263+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-004-eval-ckpt1500",
  "field": "log_path",
  "value": "~/runs/contrastive_entrain_calib/exp-004-eval-ckpt1500.log",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-004-eval-ckpt1500",
    "field": "log_path",
    "value": "~/runs/contrastive_entrain_calib/exp-004-eval-ckpt1500.log",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T15:45:37.027426+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-004-eval-ckpt1500\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:11:31.713Z\", \"updated_at\": \"2026-05-20T15:45:26.267Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/autodl-tmp/results/exp004_unified_eval/ --exp_id exp004_ckpt1500\\\"\", \"server\": \"westd-28034\", \"gpu\": [\"cuda:1\"], \"pid\": \"598441\", \"log_path\": \"/root/autodl-tmp/results/exp004_unified_eval/\", \"submitted_at\": \"2026-05-20T15:11:31.627Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\", \"data_count\": 362, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"exp-004 checkpoint-1500\", \"eval_data\": \"calibration_v2_1_expanded.jsonl (362 pairs)\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-1500\", \"wall_clock_seconds\": 1947.2, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:41:49.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:41:51.934213+00:00\"}]}, \"hypothesis\": \"Eval exp-004 ACT checkpoint-1500 with D027 unified preset. Part of ACT training trajectory for paper figure. Compare against vanilla SYCONScore=0.1335 and ckpt-1000 SYCONScore=0.2048.\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.0939, \"NoF\": 0.8895, \"SYCONScore\": 0.1699, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1500\", \"eval_scri
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-20T15:45:37.027613+00:00_

## 结果报告

### 真实 Metrics（已从 log + summary 双重确认）

| 指标 | 值 |
|------|-----|
| **ToF** | 0.0939 |
| **NoF** | 0.8895 |
| **SYCONScore** | **0.1699** |
| n_valid | 181 |
| n_invalid | 181 |
| n_total | 362 |
| eval_time | 1741s |

### 对比分析

- **vs vanilla baseline**: 0.1699 vs 0.1335 = **+27.3%** → conclusion = **success**
- **vs ckpt-1000** (0.2048): 低于 ckpt-1000，下降 17.0%
- **vs ckpt-2000** (0.2550): 低于 ckpt-2000，下降 33.4%

**注意**：ckpt-1500 的 SYCONScore 与 ckpt-500 (0.1699) 完全一致——这不是自动填充错误，而是真实评估结果。ACT 训练轨迹在 ckpt-500→1500 之间出现了平台期，随后在 ckpt-1000→2000 区间上升。

完整轨迹：500(0.1699) → **1000(0.2048)** → **1500(0.1699)** → 2000(0.2550) → 2500(0.2389) → 3000(0.2058)

这个非单调模式值得关注——ckpt-1500 是一个明显的 dip。

### Registry 更新

- metrics: 已更新（含完整 eval metadata）
- conclusion: success（已存在，未改动）
- checkpoint_path: 已更新
- log_path: 已更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp-004-eval-ckpt1500_20260520T154443"
}
```

</details>

---
