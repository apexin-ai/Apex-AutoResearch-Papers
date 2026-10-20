# code 14b rsft train launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/chats/worker_code_14b-rsft-train-launch_20260520T191246.jsonl`
- **Structured JSON:** [`9fc5744c9a59c401d3fe.json`](../../sessions/9f/9fc5744c9a59c401d3fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

97 recorded events

### Tool call

_source line 1 · 2026-05-20T19:17:36.346477+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T19:17:36.346857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T19:17:36.347042+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige/scripts/ -name \"*rsft*train*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/freige/scripts/ -name \"*rsft*train*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T19:17:36.347177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/rsft_scored_14b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/rsft_scored_14b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T19:17:36.347339+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/scripts/plan017/step3_rsft_train_14b.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:17:36.347468+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige/scripts/plan017/ -name \"*train*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/freige/scripts/plan017/ -name \"*train*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T19:17:36.347596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 84776\\ndrwxr-xr-x  2 root root       95 May 21 03:09 .\\ndrwxr-xr-x 81 root root     8192 May 21 02:10 ..\\n-rw-r--r--  1 root root     4655 May 21 03:09 rsft_report.json\\n-rw-r--r--  1 root root 77197975 May 21 03:09 rsft_scores.jsonl\\n-rw-r--r--  1 root root  9586200 May 21 03:09 rsft_train.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T19:17:36.347718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:17:36.347840+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/scripts/plan017/step3_rsft_train_14b.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:17:36.347961+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB\\n1, 18879 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:17:36.348111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/scripts/plan017/step3_rsft_train_14b.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/scripts/plan017/step3_rsft_train_14b.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:17:36.348311+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# Step 3: RSFT training for 14B (Qwen3-14B + SFT merged → RSFT LoRA)\\n# Prerequisite: SFT adapter merged into base model (ZeRO-3 incompatible with runtime merge)\\n# Uses: accelerate + DeepSpeed ZeRO-3 on 2 GPUs\\nset -euo pipefail\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\ncd /root/autodl-tmp/freige\\n\\nexport CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-2,3}}\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\nexport HF_HUB_OFFLINE=1\\nexport TRANSFORMERS_OFFLINE=1\\n\\nMERGED_MODEL=\\\"/root/autodl-tmp/models/Qwen3-14B-sft-merged\\\"\\nRSFT_DATA=\\\"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\\"\\nOUTPUT_DIR=\\\"/root/autodl-tmp/rsft_output_14b\\\"\\n\\n# --- Pre-flight checks ---\\nif [ ! -d \\\"$MERGED_MODEL\\\" ]; then\\n    echo \\\"ERROR: Merged SFT model not found at $MERGED_MODEL\\\"\\n    echo \\\"Run merge first:\\\"\\n    echo \\\"  CUDA_VISIBLE_DEVICES=0 python scripts/merge_sft_adapter_14b.py\\\"\\n    exit 1\\nfi\\n\\nif [ ! -f \\\"$RSFT_DATA\\\" ]; then\\n    echo \\\"ERROR: RSFT training data not found: $RSFT_DATA\\\"\\n    echo \\\"Ensure step2_ced_score_14b.sh has completed.\\\"\\n    exit 1\\nfi\\n\\necho \\\"=== Step 3: RSFT Training (14B) ===\\\"\\necho \\\"Base (merged): $MERGED_MODEL\\\"\\necho \\\"Data:          $RSFT_DATA\\\"\\necho \\\"Output:        $OUTPUT_DIR\\\"\\necho \\\"GPUs:          $CUDA_VISIBLE_DEVICES\\\"\\n\\naccelerate launch \\\\\\n  --config_file configs/accelerate_2gpu_zero3.yaml \\\\\\n  -m freige.training.rsft_trainer \\\\\\n  --base_model \\\"$MERGED_MODEL\\\" \\\\\\n  --sft_adapter \\\"\\\" \\\\\\n  --rsft_data_path \\\"$RSFT_DATA\\\" \\\\\\n  --output_dir \\\"$OUTPUT_DIR\\\" \\\\\\n  --deepspeed configs/deepspeed_zero3_14b.json \\\\\\n  --lora_rank 64 \\\\\\n  --lora_alpha 128 \\\\\\n  --lora_dropout 0.05 \\\\\\n  --learning_rate 2e-5 \\\\\\n  --num_epochs 3 \\\\\\n  --per_device_batch_size 1 \\\\\\n  --grad
…[truncated 406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:17:36.348475+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "wc -l /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "wc -l /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T19:17:36.348603+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3015 /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:17:36.348755+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -1 /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -1 /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T19:17:36.349105+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"input\\\": \\\"Extract all relation triples from the document. For each triple, provide the head entity, relation, tail entity, and the sentence IDs that serve as evidence. Output as a JSON list.\\\\n\\\\nDocument:\\\\n[0] Zest Airways, Inc. operated as AirAsia Zest ( formerly Asian Spirit and Zest Air), was a low - cost airline based at the Ninoy Aquino International Airport in Pasay City, Metro Manila in the Philippines.\\\\n[1] It operated scheduled domestic and international tourist services, mainly feeder services linking Manila and Cebu with 24 domestic destinations in support of the trunk route operations of other airlines.\\\\n[2] In 2013, the airline became an affiliate of Philippines AirAsia operating their brand separately.\\\\n[3] Its main base was Ninoy Aquino International Airport, Manila.\\\\n[4] The airline was founded as Asian Spirit, the first airline in the Philippines to be run as a cooperative.\\\\n[5] On August 16, 2013, the Civil Aviation Authority of the Philippines ( CAAP), the regulating body of the Government of the Republic of the Philippines for civil aviation, suspended Zest Air flights until further notice because of safety issues.\\\\n[6] Less than a year after AirAsia and Zest Air's strategic alliance, the airline has been rebranded as AirAsia Zest.\\\\n[7] The airline was merged into AirAsia Philippines in January 2016.\\\\n\\\\nEntities: Asian Spirit (ORG), Manila (LOC), Metro Manila (LOC), Ninoy Aquino International Airport (LOC), Pasay City (LOC), Philippines (LOC), Zest Air (ORG), Zest Airways, Inc. (ORG)\\\", \\\"output\\\": \\\"[{\\\\\\\"head\\\\\\\": \\\\\\\"Pasay City\\\\\\\", \\\\\\\"relation\\\\\\\": \\\\\\\"located in the administrative territorial entity\\\\\\\", \\\\\\\"tail\\\\\\\": \\\\\\\"Metro Manila\\\\\\\", \\\\\\\"evidence\\\\\\\": [0]}, {\\\\\\\"head\\\\\\\": \\\\\\\"Pasay City\\\\\\\", \\\\\\\"relation\\\\\\\": \\\\\\\"country\\\\\\\", \\\\\\\"tail\\\
…[truncated 4909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:17:36.349313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/scripts/d112/step3_rsft_train.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/scripts/d112/step3_rsft_train.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:17:36.349460+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/freige/scripts/d112/step3_rsft_train.sh: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:17:36.349584+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "du -sh /root/autodl-tmp/models/Qwen/Qwen3-14B/ /root/autodl-tmp/sft_output_14b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "du -sh /root/autodl-tmp/models/Qwen/Qwen3-14B/ /root/autodl-tmp/sft_output_14b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:17:36.349708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"56G\\t/root/autodl-tmp/models/Qwen/Qwen3-14B/\\n7.3G\\t/root/autodl-tmp/sft_output_14b/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:17:36.349834+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/rsft_scored_14b/rsft_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/rsft_scored_14b/rsft_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:17:36.350064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"total_records\\\": 24216,\\n  \\\"selected_records\\\": 3015,\\n  \\\"filtered_records\\\": 21201,\\n  \\\"selection_rate\\\": 0.12450445986124876,\\n  \\\"unique_docs_total\\\": 3027,\\n  \\\"unique_docs_selected\\\": 3015,\\n  \\\"format_reward_stats\\\": {\\n    \\\"mean\\\": 0.999587049884374,\\n    \\\"std\\\": 0.02031697782220665,\\n    \\\"min\\\": 0.0,\\n    \\\"max\\\": 1.0,\\n    \\\"median\\\": 1.0,\\n    \\\"p5\\\": 1.0,\\n    \\\"p10\\\": 1.0,\\n    \\\"p25\\\": 1.0,\\n    \\\"p75\\\": 1.0,\\n    \\\"p90\\\": 1.0,\\n    \\\"p95\\\": 1.0,\\n    \\\"histogram\\\": {\\n      \\\"counts\\\": [\\n        10,\\n        0,\\n        0,\\n        0,\\n        0,\\n        0,\\n        0,\\n        0,\\n        0,\\n        24206\\n      ],\\n      \\\"bin_edges\\\": [\\n        0.0,\\n        0.1,\\n        0.2,\\n        0.3,\\n        0.4,\\n        0.5,\\n        0.6,\\n        0.7,\\n        0.8,\\n        0.9,\\n        1.0\\n      ]\\n    }\\n  },\\n  \\\"f1_reward_stats\\\": {\\n    \\\"mean\\\": 0.615632419739391,\\n    \\\"std\\\": 0.20990730084385528,\\n    \\\"min\\\": 0.0,\\n    \\\"max\\\": 1.0,\\n    \\\"median\\\": 0.6363636363636365,\\n    \\\"p5\\\": 0.23887163561076602,\\n    \\\"p10\\\": 0.3333333333333333,\\n    \\\"p25\\\": 0.4999999999999999,\\n    \\\"p75\\\": 0.7647058823529412,\\n    \\\"p90\\\": 0.8666666666666667,\\n    \\\"p95\\\": 0.9333333333333333,\\n    \\\"histogram\\\": {\\n      \\\"counts\\\": [\\n        507,\\n        360,\\n        1023,\\n        1620,\\n        2568,\\n        4554,\\n        4571,\\n        4320,\\n        2912,\\n        1781\\n      ],\\n      \\\"bin_edges\\\": [\\n        0.0,\\n        0.1,\\n        0.2,\\n        0.3,\\n        0.4,\\n        0.5,\\n        0.6,\\n        0.7,\\n        0.8,\\n        0.9,\\n        1.0\\n      ]\\n    }\\n  },\\n  \\\"ced_reward_stats\\\": {\\n    \\\"mean\\\": 0.567540523615862,\\n    \\\"std\\\"
…[truncated 4063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:17:36.350271+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/models/Qwen3-14B-sft-merged/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/models/Qwen3-14B-sft-merged/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T19:17:36.350416+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/models/Qwen3-14B-sft-merged/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T19:17:36.350547+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -80 /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -80 /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T19:17:36.350733+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"RSFT (Rejection Sampling Fine-Tuning) 训练脚本。\\n\\n从 SFT warmup checkpoint 继续训练，使用经 CED 打分筛选的高质量生成数据。\\n流程: base model → merge SFT adapter → 新 QLoRA → 在 RSFT 数据上训练。\\n\\n输入: JSONL，每行 {\\\"doc_id\\\": ..., \\\"input\\\": ..., \\\"output\\\": ..., \\\"ced_score\\\": ..., ...}\\n输出: QLoRA adapter checkpoint\\n依赖: transformers, trl, peft, bitsandbytes, datasets\\n\\n单卡:   python -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output\\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\\\\n            -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\n\\nimport torch\\nfrom datasets import Dataset\\nfrom peft import LoraConfig, PeftModel, TaskType, get_peft_model\\nfrom torch.utils.data import WeightedRandomSampler\\nfrom transformers import (\\n    AutoModelForCausalLM,\\n    AutoTokenizer,\\n    BitsAndBytesConfig,\\n    TrainerCallback,\\n)\\nfrom trl import SFTConfig, SFTTrainer\\n\\nfrom freige.training import LLAMA3_CHAT_TEMPLATE\\nfrom freige.training.sft_trainer import SYSTEM_PROMPT\\n\\n\\ndef _apply_chat_template(tokenizer, messages, **kwargs):\\n    tmpl = getattr(tokenizer, 'chat_template', None) or ''\\n    if 'enable_thinking' not in tmpl:\\n        kwargs.pop('enable_thinking', None)\\n    return tokenizer.apply_chat_template(messages, **kwargs)\\n\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nDEFAULT_BASE_MODEL = \\\"/root/autodl-tmp/models/Qwen3-4B\\\"\\nDEFAULT_SFT_ADAPTER = \\\"/root/autodl-tmp/sft_output\\\"\\n\\n\\ndef load_rsft_data(data_path: str, tokenizer, max_length: int = 2048):\\n    \\\"\\\"\\\"加载 CED 筛选后的 RSFT 数据，格式化为 chat template 文本。\\n\\n    每行 JSONL 的 input 字段作为 user message，output 字段作为 assistant response，\\n    
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T19:17:36.350893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige/scripts/ -path \"*/d112/*rsft*\" -o -path \"*/d112/*train*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/freige/scripts/ -path \"*/d112/*rsft*\" -o -path \"*/d112/*train*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T19:17:36.351028+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/scripts/d112/eval_4b_rsft_no_evidence.sh\\n/root/autodl-tmp/freige/scripts/d112/eval_d112_rsft_bf16.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:17:36.351159+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/sft_output_14b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/sft_output_14b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T19:17:36.351307+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nadded_tokens.json\\nchat_template.jinja\\ncheckpoint-144\\ncheckpoint-96\\nmerges.txt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:17:36.351474+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"add_argument\\|def main\\|def parse\\|sft_adapter\\|base_model\\|merge\\|quantization\\|bnb\\|gradient_checkpoint\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -n \"add_argument\\|def main\\|def parse\\|sft_adapter\\|base_model\\|merge\\|quantization\\|bnb\\|gradient_checkpoint\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T19:17:36.351602+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:17:36.351719+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "wc -l /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "wc -l /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T19:17:36.351837+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"435 /root/autodl-tmp/freige/freige/training/rsft_trainer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:17:36.351951+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"add_argument\\|def main\\|merge\\|quantization\\|bnb\\|gradient_checkpoint\\|sft_adapter\\|base_model\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -n \"add_argument\\|def main\\|merge\\|quantization\\|bnb\\|gradient_checkpoint\\|sft_adapter\\|base_model\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T19:17:36.352069+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T19:17:36.352184+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"add_argument\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -n \"add_argument\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T19:17:36.352366+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"257:    parser.add_argument(\\\"--base_model\\\", type=str, default=DEFAULT_BASE_MODEL)\\n258:    parser.add_argument(\\\"--sft_adapter\\\", type=str, default=DEFAULT_SFT_ADAPTER,\\n260:    parser.add_argument(\\\"--rsft_data_path\\\", type=str, required=True,\\n262:    parser.add_argument(\\\"--output_dir\\\", type=str, required=True)\\n263:    parser.add_argument(\\\"--learning_rate\\\", type=float, default=2e-5)\\n264:    parser.add_argument(\\\"--num_epochs\\\", type=int, default=3)\\n265:    parser.add_argument(\\\"--per_device_batch_size\\\", type=int, default=4)\\n266:    parser.add_argument(\\\"--gradient_accumulation_steps\\\", type=int, default=4)\\n267:    parser.add_argument(\\\"--warmup_steps\\\", type=int, default=100)\\n268:    parser.add_argument(\\\"--save_steps\\\", type=int, default=50)\\n269:    parser.add_argument(\\\"--save_total_limit\\\", type=int, default=5)\\n270:    parser.add_argument(\\\"--max_length\\\", type=int, default=2048)\\n271:    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n272:    parser.add_argument(\\\"--wandb_project\\\", type=str, default=\\\"freige-rsft\\\")\\n273:    parser.add_argument(\\\"--wandb_run_name\\\", type=str, default=None)\\n274:    parser.add_argument(\\\"--weighted_sampling\\\", action=\\\"store_true\\\",\\n276:    parser.add_argument(\\\"--quantize\\\", action=\\\"store_true\\\",\\n278:    parser.add_argument(\\\"--lora_rank\\\", type=int, default=64)\\n279:    parser.add_argument(\\\"--lora_alpha\\\", type=int, default=128)\\n280:    parser.add_argument(\\\"--lora_dropout\\\", type=float, default=0.05)\\n281:    parser.add_argument(\\\"--bf16\\\", action=\\\"store_true\\\", default=True)\\n282:    parser.add_argument(\\\"--deepspeed\\\", type=str, default=None,\\n284:    parser.add_argument(\\\"--eval_data_dir\\\", type=str, default=None,\\n286:    parser.add_argument(\\\"--eval_max_docs\\\", type=int, default=50,\\n288:    parser.add_
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T19:17:36.352513+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"merge\\|sft_adapter\\|quantiz\\|bnb\\|gradient_check\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -n \"merge\\|sft_adapter\\|quantiz\\|bnb\\|gradient_check\" /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T19:17:36.352637+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T19:17:36.352801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -n 150 /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -n 150 /root/autodl-tmp/freige/freige/training/rsft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T19:17:36.353006+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    parser.add_argument(\\\"--eval_max_docs\\\", type=int, default=50,\\n                        help=\\\"Max dev docs for task-level eval during training\\\")\\n    parser.add_argument(\\\"--max_new_tokens\\\", type=int, default=1024)\\n    parser.add_argument(\\\"--resume_from_checkpoint\\\", type=str, default=None,\\n                        help=\\\"Path to checkpoint dir to resume training from\\\")\\n    parser.add_argument(\\\"--max_steps\\\", type=int, default=-1,\\n                        help=\\\"Override num_epochs: stop after N steps (-1 = use num_epochs)\\\")\\n    args = parser.parse_args()\\n\\n    # ZeRO-3: initialize HfDeepSpeedConfig before model loading\\n    _ds_config_obj = None\\n    if args.deepspeed:\\n        from transformers.integrations import HfDeepSpeedConfig\\n        _ds_config_obj = HfDeepSpeedConfig(args.deepspeed)\\n\\n    # W&B\\n    if args.wandb_project and \\\"WANDB_API_KEY\\\" in os.environ:\\n        os.environ[\\\"WANDB_PROJECT\\\"] = args.wandb_project\\n        if args.wandb_run_name:\\n            os.environ[\\\"WANDB_NAME\\\"] = args.wandb_run_name\\n\\n    # Tokenizer\\n    logger.info(\\\"Loading tokenizer: %s\\\", args.base_model)\\n    tokenizer = AutoTokenizer.from_pretrained(\\n        args.base_model, trust_remote_code=True, padding_side=\\\"right\\\",\\n    )\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n    if not getattr(tokenizer, \\\"chat_template\\\", None):\\n        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE\\n\\n    # Data\\n    logger.info(\\\"Loading RSFT data: %s\\\", args.rsft_data_path)\\n    train_dataset, ced_scores = load_rsft_data(\\n        args.rsft_data_path, tokenizer, args.max_length,\\n    )\\n\\n    # Model: base -> merge SFT adapter -> new LoRA\\n    logger.info(\\\"Loading base model: %s\\\", args.base_model)\\n    local_rank = int(os.environ.get(\\\"LOCAL_RANK\\\", 0))\\n    model_kw
…[truncated 4372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:17:36.353208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/sft_output_14b/checkpoint-144/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/sft_output_14b/checkpoint-144/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T19:17:36.353375+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nadded_tokens.json\\nchat_template.jinja\\nglobal_step144\\nlatest\\nmerges.txt\\nrng_state_0.pth\\nrng_state_1.pth\\nscheduler.pt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntrainer_state.json\\ntraining_args.bin\\nvocab.json\\nzero_to_fp32.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T19:17:36.353504+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'status', 'conclusion', 'hypothesis']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'status', 'conclusion', 'hypothesis']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T19:17:36.353708+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_ced_scoring\": {\"status\": \"DONE\", \"hypothesis\": \"14B model generates higher quality candidates than 4B, so CED scoring with top_k=1 should yield RSFT training data with higher F1 and CED rewards compared to 4B CED scoring results.\", \"conclusion\": \"success\"}, \"eval_llama_sft_s44_no_evidence\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA SFT s44 标准化 no-evidence eval。补齐 LLaMA SFT 3-seed evidence tax：s42 tax=-1.65pp, s43 RUNNING。s44 with-evidence ign_f1=0.4802。完成后可计算 SFT 3-seed evidence tax mean±std。\", \"conclusion\": \"success\"}, \"eval_llama_rsft_s44_no_evidence\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA RSFT s44 no-evidence eval。补齐 LLaMA RSFT 3-seed evidence tax：s42 tax=-1.88pp (ign_f1=0.5526), s43 tax=-1.16pp (ign_f1=0.5546)。s44 with-evidence ign_f1=0.5587。完成后可计算跨家族 RSFT evidence tax mean±std。\", \"conclusion\": \"success\"}, \"eval_llama_sft_s43_no_evidence\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA SFT s43 标准化 no-evidence eval。用 s43 SFT adapter + --no_evidence flag 推理，测量 per-seed evidence tax，与 s42 no-evidence eval 配对。\", \"conclusion\": \"failed\"}, \"migration_bjb2_to_westd\": {\"status\": \"DONE\", \"hypothesis\": \"全量数据迁移 bjb2-12179 → westd-37389，207G 包含所有 adapters、基座模型、数据集、eval 结果。迁移完成后 4 GPU 并行恢复实验。\", \"conclusion\": \"success\"}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"hypothesis\": \"D112 step 2: CED scoring + k=1 selection on SFT s44 generation candidates. 使用 NLI-DeBERTa 对 N=8 候选打分，format_w=0.2, f1_w=0.4, ced_w=0.4，top_k=1 筛选最优样本用于后续 RSFT 训练。\", \"conclusion\": \"success\"}, \"d112_rsft_s44_generate\": {\"status\": \"DONE\", \"hypothesis\": \"D112 step1: 用 SFT s44 adapter (ign_f1=0.4734, 最强 seed) 生成 N=8 RSFT 候选。验证 RSFT pipeline 从强 SFT base 出发是否能进一步提升，决定 Claim 1 表述强度。\", \"conclusion\": \"success\"}, \"plan017_14b_rsft_generate_r3\": {\"status\": \"DONE\", \"hypothesis\": \"14B RSFT 生成 resume (r3: 修正 adapter 路径指向 checkpoint-144)。从 doc 18
…[truncated 3445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T19:17:36.353897+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'd112_rsft_s44_train'}",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'd112_rsft_s44_train'}",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T19:17:36.354035+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'd112_rsft_s44_ced_score'}",
  "fields": "['spec']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'd112_rsft_s44_ced_score'}",
    "fields": "['spec']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T19:17:36.354163+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0049}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T19:17:36.354316+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8549}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T19:17:36.354446+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'spec']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'spec']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T19:17:36.354841+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_ced_scoring\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=0 bash scripts/plan017/step2_ced_score_14b.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"44419\", \"log_path\": \"~/runs/faith-evidence-ie/plan017_14b_ced_scoring.log\", \"submitted_at\": \"2026-05-20T18:10:17.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_scored_14b\", \"wall_clock_seconds\": 3793.4, \"gpu_hours\": 1.05}}, \"eval_llama_sft_s44_no_evidence\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path sft_output_llama_3_1_8b_s44 --no_evidence\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"meta-llama/Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s44\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/eval_llama_sft_s44_no_evidence\", \"log_path\": \"~/runs/faith-evidence-ie/eval_llama_sft_s44_no_evidence.log\"}}, \"eval_llama_rsft_s44_no_evidence\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path rsft_output_llama_3_1_8b_k1_s44 --no_evidence\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"meta-llama/Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/eval_llama_rsft_s44_no_evidence\", \"log_path\": \"~/runs/faith-evidence-ie/eval_llama_rsft_s44_no_evidence.log\", \"metrics\": {\"ign_f1\": 0.555, \
…[truncated 22432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T19:17:36.355052+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__kill_job",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__kill_job",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T19:17:36.355184+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T19:17:36.355362+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "bash -c \"tmux new-session -d -s rsft14b_dryrun 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /tmp/rsft_14b_dryrun --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 9999 --save_total_limit 1 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project none --max_steps 5 2>&1 | tee /tmp/rsft_14b_dryrun.log; echo DRYRUN_EXIT_CODE=$?' && echo 'tmux session started'\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "bash -c \"tmux new-session -d -s rsft14b_dryrun 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /tmp/rsft_14b_dryrun --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 9999 --save_total_limit 1 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project none --max_steps 5 2>&1 | tee /tmp/rsft_14b_dryrun.log; echo DRYRUN_EXIT_CODE=$?' && echo 'tmux session started'\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T19:17:36.355505+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"tmux session started\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T19:17:36.355641+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -30 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -30 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T19:17:36.355767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T19:17:36.355914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -30 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -30 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T19:17:36.356042+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 03:15:31,399 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n2026-05-21 03:15:31,854 INFO Loading RSFT data: /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:31,898 INFO Loaded 3015 RSFT samples from /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:35,398 INFO Prepared 3015 RSFT samples (CED scores: min=0.000, max=0.998, mean=0.690)\\n2026-05-21 03:15:35,468 INFO Loading base model: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T19:17:36.356180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -30 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -30 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T19:17:36.356365+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 03:15:31,399 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n2026-05-21 03:15:31,854 INFO Loading RSFT data: /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:31,898 INFO Loaded 3015 RSFT samples from /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:35,398 INFO Prepared 3015 RSFT samples (CED scores: min=0.000, max=0.998, mean=0.690)\\n2026-05-21 03:15:35,468 INFO Loading base model: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/443 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/443 [00:00<01:36,  4.57it/s]\\rLoading weights:   0%|          | 2/443 [00:00<01:46,  4.16it/s]\\rLoading weights:   2%|▏         | 8/443 [00:00<00:29, 14.92it/s]\\rLoading weights:   6%|▌         | 27/443 [00:00<00:07, 53.71it/s]\\rLoading weights:   9%|▉         | 39/443 [00:00<00:06, 65.51it/s]\\rLoading weights:  11%|█         | 48/443 [00:01<00:05, 68.78it/s]\\rLoading weights:  14%|█▎        | 60/443 [00:01<00:06, 56.11it/s]\\rLoading weights:  21%|██        | 92/443 [00:01<00:03, 106.03it/s]\\rLoading weights:  24%|██▍       | 106/443 [00:01<00:03, 103.26it/s]\\rLoading weights:  27%|██▋       | 119/443 [00:01<00:03, 107.48it/s]\\rLoading weights:  30%|██▉       | 132/443 [00:01<00:03, 89.59it/s] \\rLoading weights:  34%|███▎      | 149/443 [00:02<00:02, 100.55it/s]\\rLoading weights:  36%|███▋      | 161/443 [00:02<00:02, 99.90it/s] \\rLoading weights:  39%|███▉      | 172/443 [00:02<00:03, 71.46it/s]\\rLoading weights:  46%|████▌     | 203/443 [00:02<00:02, 113.38it/s]\\rLoading weights:  49%|████▉     | 218/443 [00:02<00:02, 82.02it/s] \\rLoading weights:  56%|█████▌    | 248/443 [00:02<00:01, 113.42it/s]\\rLoading weights:  60%|█████▉    | 264/443 [00:03<00:01, 101.36it/s]\\rLoading weights:  63%|██████▎   | 281/443 [00:03<00:01, 112.34it/s]\\rLoading w
…[truncated 372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T19:17:36.356518+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T19:17:36.356646+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 28731 MiB, 97887 MiB\\n1, 18879 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T19:17:36.356813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -40 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -40 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T19:17:36.356978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 03:15:31,399 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n2026-05-21 03:15:31,854 INFO Loading RSFT data: /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:31,898 INFO Loaded 3015 RSFT samples from /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:35,398 INFO Prepared 3015 RSFT samples (CED scores: min=0.000, max=0.998, mean=0.690)\\n2026-05-21 03:15:35,468 INFO Loading base model: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/443 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/443 [00:00<01:36,  4.57it/s]\\rLoading weights:   0%|          | 2/443 [00:00<01:46,  4.16it/s]\\rLoading weights:   2%|▏         | 8/443 [00:00<00:29, 14.92it/s]\\rLoading weights:   6%|▌         | 27/443 [00:00<00:07, 53.71it/s]\\rLoading weights:   9%|▉         | 39/443 [00:00<00:06, 65.51it/s]\\rLoading weights:  11%|█         | 48/443 [00:01<00:05, 68.78it/s]\\rLoading weights:  14%|█▎        | 60/443 [00:01<00:06, 56.11it/s]\\rLoading weights:  21%|██        | 92/443 [00:01<00:03, 106.03it/s]\\rLoading weights:  24%|██▍       | 106/443 [00:01<00:03, 103.26it/s]\\rLoading weights:  27%|██▋       | 119/443 [00:01<00:03, 107.48it/s]\\rLoading weights:  30%|██▉       | 132/443 [00:01<00:03, 89.59it/s] \\rLoading weights:  34%|███▎      | 149/443 [00:02<00:02, 100.55it/s]\\rLoading weights:  36%|███▋      | 161/443 [00:02<00:02, 99.90it/s] \\rLoading weights:  39%|███▉      | 172/443 [00:02<00:03, 71.46it/s]\\rLoading weights:  46%|████▌     | 203/443 [00:02<00:02, 113.38it/s]\\rLoading weights:  49%|████▉     | 218/443 [00:02<00:02, 82.02it/s] \\rLoading weights:  56%|█████▌    | 248/443 [00:02<00:01, 113.42it/s]\\rLoading weights:  60%|█████▉    | 264/443 [00:03<00:01, 101.36it/s]\\rLoading weights:  63%|██████▎   | 281/443 [00:03<00:01, 112.34it/s]\\rLoading w
…[truncated 1219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T19:17:36.357161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -20 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -20 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T19:17:36.357369+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 03:15:31,399 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n2026-05-21 03:15:31,854 INFO Loading RSFT data: /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:31,898 INFO Loaded 3015 RSFT samples from /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\n2026-05-21 03:15:35,398 INFO Prepared 3015 RSFT samples (CED scores: min=0.000, max=0.998, mean=0.690)\\n2026-05-21 03:15:35,468 INFO Loading base model: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/443 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/443 [00:00<01:36,  4.57it/s]\\rLoading weights:   0%|          | 2/443 [00:00<01:46,  4.16it/s]\\rLoading weights:   2%|▏         | 8/443 [00:00<00:29, 14.92it/s]\\rLoading weights:   6%|▌         | 27/443 [00:00<00:07, 53.71it/s]\\rLoading weights:   9%|▉         | 39/443 [00:00<00:06, 65.51it/s]\\rLoading weights:  11%|█         | 48/443 [00:01<00:05, 68.78it/s]\\rLoading weights:  14%|█▎        | 60/443 [00:01<00:06, 56.11it/s]\\rLoading weights:  21%|██        | 92/443 [00:01<00:03, 106.03it/s]\\rLoading weights:  24%|██▍       | 106/443 [00:01<00:03, 103.26it/s]\\rLoading weights:  27%|██▋       | 119/443 [00:01<00:03, 107.48it/s]\\rLoading weights:  30%|██▉       | 132/443 [00:01<00:03, 89.59it/s] \\rLoading weights:  34%|███▎      | 149/443 [00:02<00:02, 100.55it/s]\\rLoading weights:  36%|███▋      | 161/443 [00:02<00:02, 99.90it/s] \\rLoading weights:  39%|███▉      | 172/443 [00:02<00:03, 71.46it/s]\\rLoading weights:  46%|████▌     | 203/443 [00:02<00:02, 113.38it/s]\\rLoading weights:  49%|████▉     | 218/443 [00:02<00:02, 82.02it/s] \\rLoading weights:  56%|█████▌    | 248/443 [00:02<00:01, 113.42it/s]\\rLoading weights:  60%|█████▉    | 264/443 [00:03<00:01, 101.36it/s]\\rLoading weights:  63%|██████▎   | 281/443 [00:03<00:01, 112.34it/s]\\rLoading w
…[truncated 4260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T19:17:36.357524+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T19:17:36.357658+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 35069 MiB, 97887 MiB\\n1, 18879 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T19:17:36.357809+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -10 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -10 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T19:17:36.357986+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 03:15:35,468 INFO Loading base model: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/443 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/443 [00:00<01:36,  4.57it/s]\\rLoading weights:   0%|          | 2/443 [00:00<01:46,  4.16it/s]\\rLoading weights:   2%|▏         | 8/443 [00:00<00:29, 14.92it/s]\\rLoading weights:   6%|▌         | 27/443 [00:00<00:07, 53.71it/s]\\rLoading weights:   9%|▉         | 39/443 [00:00<00:06, 65.51it/s]\\rLoading weights:  11%|█         | 48/443 [00:01<00:05, 68.78it/s]\\rLoading weights:  14%|█▎        | 60/443 [00:01<00:06, 56.11it/s]\\rLoading weights:  21%|██        | 92/443 [00:01<00:03, 106.03it/s]\\rLoading weights:  24%|██▍       | 106/443 [00:01<00:03, 103.26it/s]\\rLoading weights:  27%|██▋       | 119/443 [00:01<00:03, 107.48it/s]\\rLoading weights:  30%|██▉       | 132/443 [00:01<00:03, 89.59it/s] \\rLoading weights:  34%|███▎      | 149/443 [00:02<00:02, 100.55it/s]\\rLoading weights:  36%|███▋      | 161/443 [00:02<00:02, 99.90it/s] \\rLoading weights:  39%|███▉      | 172/443 [00:02<00:03, 71.46it/s]\\rLoading weights:  46%|████▌     | 203/443 [00:02<00:02, 113.38it/s]\\rLoading weights:  49%|████▉     | 218/443 [00:02<00:02, 82.02it/s] \\rLoading weights:  56%|█████▌    | 248/443 [00:02<00:01, 113.42it/s]\\rLoading weights:  60%|█████▉    | 264/443 [00:03<00:01, 101.36it/s]\\rLoading weights:  63%|██████▎   | 281/443 [00:03<00:01, 112.34it/s]\\rLoading weights:  67%|██████▋   | 295/443 [00:03<00:01, 114.11it/s]\\rLoading weights:  70%|██████▉   | 309/443 [00:03<00:01, 111.82it/s]\\rLoading weights:  73%|███████▎  | 322/443 [00:03<00:01, 111.28it/s]\\rLoading weights:  75%|███████▌  | 334/443 [00:03<00:01, 92.98it/s] \\rLoading weights:  78%|███████▊  | 345/443 [00:04<00:01, 68.61it/s]\\rLoading weights:  86%|████████▌ | 379/443 [00:04<00:00, 111.34it/
…[truncated 3951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T19:17:36.358135+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T19:17:36.358281+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 38019 MiB, 97887 MiB\\n1, 18879 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T19:17:36.358453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -10 /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -10 /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T19:17:36.358744+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/443 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/443 [00:00<01:36,  4.57it/s]\\rLoading weights:   0%|          | 2/443 [00:00<01:46,  4.16it/s]\\rLoading weights:   2%|▏         | 8/443 [00:00<00:29, 14.92it/s]\\rLoading weights:   6%|▌         | 27/443 [00:00<00:07, 53.71it/s]\\rLoading weights:   9%|▉         | 39/443 [00:00<00:06, 65.51it/s]\\rLoading weights:  11%|█         | 48/443 [00:01<00:05, 68.78it/s]\\rLoading weights:  14%|█▎        | 60/443 [00:01<00:06, 56.11it/s]\\rLoading weights:  21%|██        | 92/443 [00:01<00:03, 106.03it/s]\\rLoading weights:  24%|██▍       | 106/443 [00:01<00:03, 103.26it/s]\\rLoading weights:  27%|██▋       | 119/443 [00:01<00:03, 107.48it/s]\\rLoading weights:  30%|██▉       | 132/443 [00:01<00:03, 89.59it/s] \\rLoading weights:  34%|███▎      | 149/443 [00:02<00:02, 100.55it/s]\\rLoading weights:  36%|███▋      | 161/443 [00:02<00:02, 99.90it/s] \\rLoading weights:  39%|███▉      | 172/443 [00:02<00:03, 71.46it/s]\\rLoading weights:  46%|████▌     | 203/443 [00:02<00:02, 113.38it/s]\\rLoading weights:  49%|████▉     | 218/443 [00:02<00:02, 82.02it/s] \\rLoading weights:  56%|█████▌    | 248/443 [00:02<00:01, 113.42it/s]\\rLoading weights:  60%|█████▉    | 264/443 [00:03<00:01, 101.36it/s]\\rLoading weights:  63%|██████▎   | 281/443 [00:03<00:01, 112.34it/s]\\rLoading weights:  67%|██████▋   | 295/443 [00:03<00:01, 114.11it/s]\\rLoading weights:  70%|██████▉   | 309/443 [00:03<00:01, 111.82it/s]\\rLoading weights:  73%|███████▎  | 322/443 [00:03<00:01, 111.28it/s]\\rLoading weights:  75%|███████▌  | 334/443 [00:03<00:01, 92.98it/s] \\rLoading weights:  78%|███████▊  | 345/443 [00:04<00:01, 68.61it/s]\\rLoading weights:  86%|████████▌ | 379/443 [00:04<00:00, 111.34it/s]\\rLoading weights:  89%|████████▊ | 393/443 [00:04<00:00, 103.20it/s]\\rLoading weights
…[truncated 4223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T19:17:36.358967+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tmux kill-session -t rsft14b_dryrun 2>/dev/null; rm -rf /tmp/rsft_14b_dryrun /tmp/rsft_14b_dryrun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tmux kill-session -t rsft14b_dryrun 2>/dev/null; rm -rf /tmp/rsft_14b_dryrun /tmp/rsft_14b_dryrun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T19:17:36.359107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T19:17:36.359317+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_train",
  "field": "hypothesis",
  "value": "14B RSFT LoRA training on CED-scored top_k=1 data (3015 samples). 14B SFT (ign_f1=0.5507) as base, expect RSFT to further improve via rejection sampling on high-quality generations. Completes scaling table 4th row (1.7B→4B→8B→14B).",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_train",
    "field": "hypothesis",
    "value": "14B RSFT LoRA training on CED-scored top_k=1 data (3015 samples). 14B SFT (ign_f1=0.5507) as base, expect RSFT to further improve via rejection sampling on high-quality generations. Completes scaling table 4th row (1.7B→4B→8B→14B).",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T19:17:36.359517+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_train\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:16:38.313Z\", \"updated_at\": \"2026-05-20T19:16:38.313Z\", \"hypothesis\": \"14B RSFT LoRA training on CED-scored top_k=1 data (3015 samples). 14B SFT (ign_f1=0.5507) as base, expect RSFT to further improve via rejection sampling on high-quality generations. Completes scaling table 4th row (1.7B→4B→8B→14B).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3005}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T19:17:36.359660+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "mkdir -p ~/runs/faith-evidence-ie && tmux new-session -d -s plan017_14b_rsft_train 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017 2>&1 | tee ~/runs/faith-evidence-ie/plan017_14b_rsft_train.log' && sleep 3 && tmux list-panes -t plan017_14b_rsft_train -F \"#{pane_pid}\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "mkdir -p ~/runs/faith-evidence-ie && tmux new-session -d -s plan017_14b_rsft_train 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017 2>&1 | tee ~/runs/faith-evidence-ie/plan017_14b_rsft_train.log' && sleep 3 && tmux list-panes -t plan017_14b_rsft_train -F \"#{pane_pid}\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T19:17:36.359795+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"48799\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-20T19:17:36.359945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps --ppid 48799 -o pid=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps --ppid 48799 -o pid=",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T19:17:36.360070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \" 48806\\n 48807\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-20T19:17:36.360188+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps -p 48806,48807 -o pid,comm=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps -p 48806,48807 -o pid,comm=",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T19:17:36.360341+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID \\n 48806 python\\n 48807 tee\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-20T19:17:36.360493+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_train",
  "field": "status",
  "value": "RUNNING",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017\"', 'server': 'rtx5090-4x', 'gpu': ['cuda:0'], 'pid': '48806', 'log_path': '~/runs/faith-evidence-ie/plan017_14b_rsft_train.log', 'submitted_at': '2026-05-20T19:16:50Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl', 'data_count': 3015, 'model_name': 'Qwen3-14B', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/sft_output_14b/checkpoint-144', 'checkpoint_path': '/root/autodl-tmp/rsft_output_14b'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_train",
    "field": "status",
    "value": "RUNNING",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017\"', 'server': 'rtx5090-4x', 'gpu': ['cuda:0'], 'pid': '48806', 'log_path': '~/runs/faith-evidence-ie/plan017_14b_rsft_train.log', 'submitted_at': '2026-05-20T19:16:50Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl', 'data_count': 3015, 'model_name': 'Qwen3-14B', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/sft_output_14b/checkpoint-144', 'checkpoint_path': '/root/autodl-tmp/rsft_output_14b'}"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T19:17:36.360649+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.7906}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-20T19:17:36.360853+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_train",
  "field": "status",
  "value": "QUEUED",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_train",
    "field": "status",
    "value": "QUEUED",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T19:17:36.360993+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_train\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:16:38.313Z\", \"updated_at\": \"2026-05-20T19:17:10.074Z\", \"hypothesis\": \"14B RSFT LoRA training on CED-scored top_k=1 data (3015 samples). 14B SFT (ign_f1=0.5507) as base, expect RSFT to further improve via rejection sampling on high-quality generations. Completes scaling table 4th row (1.7B→4B→8B→14B).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.497}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-20T19:17:36.361128+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_train",
  "field": "status",
  "value": "RUNNING",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017\"', 'server': 'rtx5090-4x', 'gpu': ['cuda:0'], 'pid': '48806', 'log_path': '~/runs/faith-evidence-ie/plan017_14b_rsft_train.log', 'submitted_at': '2026-05-20T19:16:50Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl', 'data_count': 3015, 'model_name': 'Qwen3-14B', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/sft_output_14b/checkpoint-144', 'checkpoint_path': '/root/autodl-tmp/rsft_output_14b'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_train",
    "field": "status",
    "value": "RUNNING",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017\"', 'server': 'rtx5090-4x', 'gpu': ['cuda:0'], 'pid': '48806', 'log_path': '~/runs/faith-evidence-ie/plan017_14b_rsft_train.log', 'submitted_at': '2026-05-20T19:16:50Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl', 'data_count': 3015, 'model_name': 'Qwen3-14B', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/sft_output_14b/checkpoint-144', 'checkpoint_path': '/root/autodl-tmp/rsft_output_14b'}"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-20T19:17:36.361369+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_train\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:16:38.313Z\", \"updated_at\": \"2026-05-20T19:17:19.517Z\", \"hypothesis\": \"14B RSFT LoRA training on CED-scored top_k=1 data (3015 samples). 14B SFT (ign_f1=0.5507) as base, expect RSFT to further improve via rejection sampling on high-quality generations. Completes scaling table 4th row (1.7B→4B→8B→14B).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --rsft_data_path /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_14b --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft-14b-plan017\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"48806\", \"log_path\": \"~/runs/faith-evidence-ie/plan017_14b_rsft_train.log\", \"submitted_at\": \"2026-05-20T19:16:50Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"data_count\": 3015, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_14b/checkpoint-144\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_14b\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4487}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-20T19:17:36.361557+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -5 ~/runs/faith-evidence-ie/plan017_14b_rsft_train.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -5 ~/runs/faith-evidence-ie/plan017_14b_rsft_train.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-20T19:17:36.361687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-20T19:17:36.361859+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\rAdding EOS to train dataset:   0%|          | 0/3015 [00:00<?, ? examples/s]\\rAdding EOS to train dataset: 100%|██████████| 3015/3015 [00:00<00:00, 46281.87 examples/s]\\n\\rTokenizing train dataset:   0%|          | 0/3015 [00:00<?, ? examples/s]\\rTokenizing train dataset:   3%|▎         | 105/3015 [00:00<00:02, 1028.18 examples/s]\\rTokenizing train dataset:   7%|▋         | 210/3015 [00:00<00:02, 1035.03 examples/s]\\rTokenizing train dataset:  12%|█▏        | 352/3015 [00:00<00:02, 979.49 examples/s] \\rTokenizing train dataset:  16%|█▌        | 485/3015 [00:00<00:02, 935.72 examples/s]\\rTokenizing train dataset:  21%|██        | 622/3015 [00:00<00:02, 919.40 examples/s]\\rTokenizing train dataset:  25%|██▌       | 758/3015 [00:00<00:02, 909.36 examples/s]\\rTokenizing train dataset:  28%|██▊       | 856/3015 [00:00<00:02, 924.80 examples/s]\\rTokenizing train dataset:  33%|███▎      | 986/3015 [00:01<00:02, 900.87 examples/s]\\rTokenizing train dataset:  36%|███▌      | 1089/3015 [00:01<00:02, 726.11 examples/s]\\rTokenizing train dataset:  39%|███▉      | 1177/3015 [00:01<00:02, 752.13 examples/s]\\rTokenizing train dataset:  42%|████▏     | 1267/3015 [00:01<00:02, 785.13 examples/s]\\rTokenizing train dataset:  45%|████▍     | 1354/3015 [00:01<00:02, 802.40 examples/s]\\rTokenizing train dataset:  48%|████▊     | 1448/3015 [00:01<00:01, 835.15 examples/s]\\rTokenizing train dataset:  51%|█████     | 1543/3015 [00:01<00:01, 865.17 examples/s]\\rTokenizing train dataset:  54%|█████▍    | 1638/3015 [00:01<00:01, 882.17 examples/s]\\rTokenizing train dataset:  57%|█████▋    | 1728/3015 [00:01<00:01, 883.16 examples/s]\\rTokenizing train dataset:  60%|██████    | 1819/3015 [00:02<00:01, 888.60 examples/s]\\rTokenizing train dataset:  65%|██████▍   | 1954/3015 [00:02<00:01, 890.43 examples/s]\\rTokenizing train dataset:  69%|██████��   | 2081/3015 [00:02<00:01, 803.90 examples/s]\\rTokenizing train datas
…[truncated 1592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T19:17:36.362012+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 38021 MiB, 97887 MiB\\n1, 18879 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 97 · 2026-05-20T19:17:36.362182+00:00_

训练已正常运行。

## 汇报

| 项目 | 值 |
|------|-----|
| **exp_id** | `plan017_14b_rsft_train` |
| **PID** | 48806 |
| **GPU** | cuda:0, 峰值显存 38GB / 96GB |
| **训练数据** | 3015 条 (CED top_k=1) |
| **Base model** | Qwen3-14B + SFT adapter (checkpoint-144) merge |
| **LoRA rank/alpha** | 64 / 128 |
| **Trainable params** | 256.9M / 15.0B (1.71%) |
| **Epochs** | 3 |
| **LR** | 2e-5 |
| **Batch size** | 1 × grad_accum 8 = effective 8 |
| **Gradient checkpointing** | Yes (硬编码) |
| **Total steps** | 1131 |
| **步速** | ~3.9s/step |
| **预估训练时间** | 1131 × 3.9s ≈ 4411s ≈ **~74 分钟 (1.2h)** |
| **预估完成时间** | ~2026-05-21 04:32 UTC |
| **Output dir** | `/root/autodl-tmp/rsft_output_14b` |
| **Log** | `~/runs/faith-evidence-ie/plan017_14b_rsft_train.log` |

不需要 QLoRA 量化，bf16 单卡 38GB 峰值，余量充足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_14b-rsft-train-launch_20260520T191246"
}
```

</details>

---
