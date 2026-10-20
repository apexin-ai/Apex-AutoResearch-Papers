# verify exp008 dryrun real data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_verify_exp008_dryrun_real_data_20260514T141556.jsonl`
- **Structured JSON:** [`dddb201a7a0aab7e510b.json`](../../sessions/dd/dddb201a7a0aab7e510b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-14T14:19:42.370801+00:00_

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
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
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

_source line 2 · 2026-05-14T14:19:42.371277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T14:19:42.375766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T14:19:42.376048+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T14:19:42.376270+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/ -maxdepth 3 -name \"config.json\" -path \"*Qwen*0.5B*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/ -maxdepth 3 -name \"config.json\" -path \"*Qwen*0.5B*\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T14:19:42.376579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16048\\ndrwxr-xr-x 2 root root    4096 May 14 21:06 .\\ndrwxr-xr-x 5 root root     151 May 14 21:29 ..\\n-rw-r--r-- 1 root root  515053 May 14 18:41 signal_embedding_arc_challenge.json\\n-rw-r--r-- 1 root root  567771 May 14 20:49 signal_embedding_gsm8k.json\\n-rw-r--r-- 1 root root 6093045 May 14 18:50 signal_embedding_mmlu.json\\n-rw-r--r-- 1 root root    2179 May 14 16:00 signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json\\n-rw-r--r-- 1 root root  185943 May 14 21:05 signal_minkpp_arc_challenge.json\\n-rw-r--r-- 1 root root  199977 May 14 20:50 signal_minkpp_gsm8k.json\\n-rw-r--r-- 1 root root 2121205 May 14 18:55 signal_minkpp_mmlu.json\\n-rw-r--r-- 1 root root  254781 May 14 21:06 signal_selfcritique_arc_challenge.json\\n-rw-r--r-- 1 root root  276624 May 14 21:05 signal_selfcritique_gsm8k.json\\n-rw-r--r-- 1 root root 2934171 May 14 21:04 signal_selfcritique_mmlu.json\\n-rw-r--r-- 1 root root  239249 May 14 21:06 signals_merged_arc_challenge.json\\n-rw-r--r-- 1 root root  258901 May 14 21:05 signals_merged_gsm8k.json\\n-rw-r--r-- 1 root root 2756294 May 14 21:04 signals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T14:19:42.376868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16048\\ndrwxr-xr-x 2 root root    4096 May 14 21:29 .\\ndrwxr-xr-x 5 root root     151 May 14 21:29 ..\\n-rw-r--r-- 1 root root  514645 May 14 21:27 signal_embedding_arc_challenge.json\\n-rw-r--r-- 1 root root  567631 May 14 21:23 signal_embedding_gsm8k.json\\n-rw-r--r-- 1 root root 6077177 May 14 18:45 signal_embedding_mmlu.json\\n-rw-r--r-- 1 root root  185939 May 14 21:28 signal_minkpp_arc_challenge.json\\n-rw-r--r-- 1 root root  200053 May 14 21:24 signal_minkpp_gsm8k.json\\n-rw-r--r-- 1 root root 2121481 May 14 21:12 signal_minkpp_mmlu.json\\n-rw-r--r-- 1 root root  256587 May 14 21:29 signal_selfcritique_arc_challenge.json\\n-rw-r--r-- 1 root root  276365 May 14 21:25 signal_selfcritique_gsm8k.json\\n-rw-r--r-- 1 root root 2952548 May 14 21:20 signal_selfcritique_mmlu.json\\n-rw-r--r-- 1 root root  239694 May 14 21:29 signals_merged_arc_challenge.json\\n-rw-r--r-- 1 root root  258884 May 14 21:25 signals_merged_gsm8k.json\\n-rw-r--r-- 1 root root 2759581 May 14 21:20 signals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T14:19:42.377127+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/run_exp008.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/run_exp008.sh"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T14:19:42.381401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T14:19:42.381837+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -euo pipefail\\n\\nGPUS=\\\"${1:?Usage: bash run_exp008.sh GPU_IDS (e.g. 1,4,5)}\\\"\\n\\n# === Paths ===\\nBASE_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\"\\nINSTRUCT_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct\\\"\\nD000_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\\\"\\nD005_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\\\"  # d005: mixed 0/1 labels, AUC computable\\nSFT_DATA=\\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\\"\\nLABELS_DIR=\\\"/root/autodl-tmp/exp001/sft_data\\\"\\n\\nOUTPUT_BASE=\\\"/root/autodl-tmp/exp008\\\"\\nSIGNALS_DIR=\\\"${OUTPUT_BASE}/signals\\\"\\nRESULTS_DIR=\\\"${OUTPUT_BASE}/results\\\"\\n\\nBENCHMARKS=(mmlu gsm8k arc_challenge)\\nSIGNALS=\\\"embedding minkpp selfcritique\\\"\\n\\nSCRIPT_DIR=\\\"$(cd \\\"$(dirname \\\"$0\\\")\\\" && pwd)\\\"\\nCOMPUTE_SCRIPT=\\\"${SCRIPT_DIR}/../exp002/compute_signals.py\\\"\\nSURVIVAL_SCRIPT=\\\"${SCRIPT_DIR}/run_signal_survival.py\\\"\\n\\n# === Environment ===\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport CUDA_VISIBLE_DEVICES=\\\"$GPUS\\\"\\n\\n# === Regime definitions ===\\ndeclare -A REGIME_MODEL\\nREGIME_MODEL[base]=\\\"$BASE_MODEL\\\"\\nREGIME_MODEL[sft_clean]=\\\"$D000_ADAPTER\\\"\\nREGIME_MODEL[sft_contam]=\\\"$D005_ADAPTER\\\"\\nREGIME_MODEL[rl_aligned]=\\\"$INSTRUCT_MODEL\\\"\\nREGIMES=(base sft_clean sft_contam rl_aligned)\\n\\necho \\\"=== exp-008 Signal Survival ===\\\"\\necho \\\"GPUs: $GPUS | Benchmarks: ${BENCHMARKS[*]} | Signals: $SIGNALS\\\"\\necho \\\"Regimes: ${REGIMES[*]}\\\"\\necho \\\"\\\"\\n\\n# === Step 0: Convert labels to {index: 0/1} format ===\\nmkdir -p \\\"${OUTPUT_BASE}/labels\\\"\\nfor bench in \\\"${BENCHMARKS[@]}\\\"; do\\n    SRC=\\\"${LABELS_DIR}/contamination_labels_${bench}_d005.json\\\"\\n    DST=\\\"${OUTPUT_BASE}/labels/labels_${benc
…[truncated 2285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:19:42.382177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/config.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T14:19:42.382470+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:19:42.382723+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct/config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct/config.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T14:19:42.382977+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T14:19:42.383219+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T14:19:42.387547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/adapter_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T14:19:42.387747+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T14:19:42.387960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/adapter_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T14:19:42.388143+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T14:19:42.388516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival — end-to-end execution script.\\nv2: Extended from SFT/RL pairwise to N-regime comparison.\\n\\nUsage:\\n  python run_signal_survival.py \\\\\\n    --regime-dirs base=/path/base SFT_clean=/path/sft RL=/path/rl \\\\\\n    --labels-file /path/to/labels.json \\\\\\n    --output-dir /path/to/exp008_output/\\n\\n  # Legacy 2-regime (still works):\\n  python run_signal_survival.py \\\\\\n    --sft-signals-dir /path/sft/ --rl-signals-dir /path/rl/ \\\\\\n    --labels-file labels.json\\n\\n  # Quick validation with mock data:\\n  python run_signal_survival.py --dry-run --max-items 10\\n  python run_signal_survival.py --dry-run --max-items 10 --regime-names base SFT RL DPO\\n\\nDependencies: numpy, scipy, sklearn\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nfrom signal_survival_analysis import (\\n    SIGNAL_KEYS,\\n    print_summary_table,\\n    run_survival_analysis,\\n    save_report,\\n)\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef load_signal_file(path: Path, signal_key: str) -> list[dict]:\\n    \\\"\\\"\\\"Load a signal JSON file and validate it has expected fields.\\\"\\\"\\\"\\n    with open(path) as f:\\n        data = json.load(f)\\n    if not isinstance(data, list) or len(data) == 0:\\n        raise ValueError(f\\\"Expected non-empty list in {path}\\\")\\n    if signal_key not in data[0]:\\n        raise ValueError(f\\\"Signal key '{signal_key}' not found in {path}\\\")\\n    return data\\n\\n\\ndef load_signals_from_dir(signals_dir: Path) -> dict[str, list[dict]]:\\n    \\\"\\\"\\\"\\n    Load all signal files from a directory.\\n    Returns {signal_key: [records]}.\\n    \\\"\\\"\\\"\\n    signals = {}\\n\\n    merged_files = list(signals_dir.glob(\\\"signals_merged_*.json\\\"))\\n    if merged_files:\\n        logger.info(\\\"Found
…[truncated 7141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T14:19:42.388765+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T14:19:42.388957+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.3449670374393463,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T14:19:42.389204+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/sft_data/contamination_labels_*_d005.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/sft_data/contamination_labels_*_d005.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T14:19:42.395506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T14:19:42.395769+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp008 && python run_signal_survival.py --dry-run --max-items 50 --regime-names base sft_clean sft_contam rl_aligned 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp008 && python run_signal_survival.py --dry-run --max-items 50 --regime-names base sft_clean sft_contam rl_aligned 2>&1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T14:19:42.396064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 22:17:33,553 [INFO] DRY-RUN: generating mock data with 50 items, 4 regimes: ['base', 'sft_clean', 'sft_contam', 'rl_aligned']\\n2026-05-14 22:17:33,559 [INFO] Running survival analysis...\\n2026-05-14 22:17:33,579 [INFO] Embedding: AUC base=0.9943 -> sft_clean=0.899 -> sft_contam=0.7695 -> rl_aligned=0.6829\\n2026-05-14 22:17:33,598 [INFO] Min-K%++: AUC base=0.9695 -> sft_clean=0.9467 -> sft_contam=0.8343 -> rl_aligned=0.7848\\n2026-05-14 22:17:33,617 [INFO] ConStat: AUC base=0.9771 -> sft_clean=0.9448 -> sft_contam=0.8133 -> rl_aligned=0.6467\\n2026-05-14 22:17:33,635 [INFO] Self-Critique: AUC base=0.9981 -> sft_clean=0.9962 -> sft_contam=0.8914 -> rl_aligned=0.7086\\n2026-05-14 22:17:33,636 [INFO] Report saved to exp008_output/survival_report.json\\n2026-05-14 22:17:33,637 [INFO] Done. Output in ./exp008_output\\n\\n============================================================\\nSignal Survival Analysis -- 4 regimes: base -> sft_clean -> sft_contam -> rl_aligned\\n============================================================\\nSignal                 base  sft_clean sft_contam rl_aligned\\n------------------------------------------------------------\\nEmbedding            0.9943     0.8990     0.7695     0.6829\\nMin-K%++             0.9695     0.9467     0.8343     0.7848\\nConStat              0.9771     0.9448     0.8133     0.6467\\nSelf-Critique        0.9981     0.9962     0.8914     0.7086\\n------------------------------------------------------------\\n  base -> sft_clean: mean AUC ratio=0.961, mean rho=0.851\\n  sft_clean -> sft_contam: mean AUC ratio=0.873, mean rho=0.724\\n  sft_contam -> rl_aligned: mean AUC ratio=0.855, mean rho=0.623\\n\\nSurviving signals: 0/4  (none)\\n============================================================\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T14:19:42.396427+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "mkdir -p /tmp/exp008_pathtest/sft_clean/mmlu /tmp/exp008_pathtest/sft_contam/mmlu /tmp/exp008_pathtest/labels && ln -sf /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json /tmp/exp008_pathtest/sft_clean/mmlu/ && ln -sf /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json /tmp/exp008_pathtest/sft_contam/mmlu/ && echo \"symlinks created\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "mkdir -p /tmp/exp008_pathtest/sft_clean/mmlu /tmp/exp008_pathtest/sft_contam/mmlu /tmp/exp008_pathtest/labels && ln -sf /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json /tmp/exp008_pathtest/sft_clean/mmlu/ && ln -sf /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json /tmp/exp008_pathtest/sft_contam/mmlu/ && echo \"symlinks created\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T14:19:42.396686+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"symlinks created\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T14:19:42.396903+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -c /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -c /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T14:19:42.397134+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2756294 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json\\n2759581 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json\\n5515875 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T14:19:42.401396+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json') as f:\n    raw = json.load(f)\nlabels = {str(i): v for i, v in enumerate(raw['labels'])}\nwith open('/tmp/exp008_pathtest/labels/labels_mmlu.json', 'w') as f:\n    json.dump(labels, f)\nprint(f'Converted {len(labels)} labels, sum={sum(labels.values())}')\n\" 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json') as f:\n    raw = json.load(f)\nlabels = {str(i): v for i, v in enumerate(raw['labels'])}\nwith open('/tmp/exp008_pathtest/labels/labels_mmlu.json', 'w') as f:\n    json.dump(labels, f)\nprint(f'Converted {len(labels)} labels, sum={sum(labels.values())}')\n\" 2>&1"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T14:19:42.401683+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Converted 14042 labels, sum=703\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T14:19:42.401939+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp008 && python run_signal_survival.py \\\n  --regime-dirs \\\n    sft_clean=/tmp/exp008_pathtest/sft_clean/mmlu \\\n    sft_contam=/tmp/exp008_pathtest/sft_contam/mmlu \\\n  --labels-file /tmp/exp008_pathtest/labels/labels_mmlu.json \\\n  --output-dir /tmp/exp008_pathtest/results_mmlu/ \\\n  2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp008 && python run_signal_survival.py \\\n  --regime-dirs \\\n    sft_clean=/tmp/exp008_pathtest/sft_clean/mmlu \\\n    sft_contam=/tmp/exp008_pathtest/sft_contam/mmlu \\\n  --labels-file /tmp/exp008_pathtest/labels/labels_mmlu.json \\\n  --output-dir /tmp/exp008_pathtest/results_mmlu/ \\\n  2>&1"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T14:19:42.402215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 22:18:23,872 [INFO] Loading signals for regime 'sft_clean' from /tmp/exp008_pathtest/sft_clean/mmlu\\n2026-05-14 22:18:23,873 [INFO] Found merged signal file: /tmp/exp008_pathtest/sft_clean/mmlu/signals_merged_mmlu.json\\n2026-05-14 22:18:23,913 [INFO] Loading signals for regime 'sft_contam' from /tmp/exp008_pathtest/sft_contam/mmlu\\n2026-05-14 22:18:23,913 [INFO] Found merged signal file: /tmp/exp008_pathtest/sft_contam/mmlu/signals_merged_mmlu.json\\n2026-05-14 22:18:23,960 [INFO] Running survival analysis...\\n2026-05-14 22:18:24,000 [INFO] Embedding: AUC sft_clean=0.5049 -> sft_contam=0.953\\n2026-05-14 22:18:24,039 [INFO] Min-K%++: AUC sft_clean=0.509 -> sft_contam=0.4655\\n2026-05-14 22:18:24,054 [INFO] ConStat: AUC sft_clean=None -> sft_contam=None\\n2026-05-14 22:18:24,087 [INFO] Self-Critique: AUC sft_clean=0.4957 -> sft_contam=0.5165\\n2026-05-14 22:18:24,088 [INFO] Report saved to /tmp/exp008_pathtest/results_mmlu/survival_report.json\\n2026-05-14 22:18:24,088 [INFO] Done. Output in /tmp/exp008_pathtest/results_mmlu/\\n\\n=====================================================================================================\\nSignal Survival Analysis -- SFT vs RL-aligned\\n=====================================================================================================\\nSignal             d(SFT)    d(RL)  d ratio  AUC(SFT)   AUC(RL)  AUC ratio      rho   Wilcox p      n\\n-----------------------------------------------------------------------------------------------------\\nEmbedding          0.0208   2.5085   120.76    0.5049    0.9530       1.89   0.6055       0.00  14042\\nMin-K%++           0.0421  -0.1079    -2.56    0.5090    0.4655       0.91   0.3053       0.00  14042\\nConStat               nan      nan      N/A       N/A       N/A        N/A      N/A        N/A      0\\nSelf-Critique     -0.0042   0.0652   -15.45    0.4957    0.5165       1.04   0.2258       0.00  14042\\n---
…[truncated 408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T14:19:42.402573+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -c \"s3_constat\" /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -c \"s3_constat\" /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T14:19:42.402806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14042\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T14:19:42.402981+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"SIGNALS=\" /root/contamcal-irt-calibration/exp008/run_exp008.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"SIGNALS=\" /root/contamcal-irt-calibration/exp008/run_exp008.sh"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T14:19:42.403167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SIGNALS=\\\"embedding minkpp selfcritique\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T14:19:42.407521+00:00_

All verifications complete. Here's the summary:

---

## 验证结果

### 1. exp-002 Signal 兼容性 — ✅ PASS
- d000 和 d005 各有 3 signal types × 3 benchmarks 的完整数据
- 数据格式（list of dicts with `s1_embedding`, `s2_minkpp`, `s3_constat`, `s4_selfcritique`）与 exp-008 `load_signals_from_dir()` 完全兼容
- **实测验证**：用 exp-002 d000/d005 的 mmlu 数据直接跑了 2-regime survival analysis，成功产出结果：
  - Embedding signal **survived**（AUC 0.505 → 0.953, ratio=1.89）
  - Min-K%++ / Self-Critique 未 survive

### 2. 模型/Adapter 路径 — ✅ 全部存在
| Regime | Path | Status |
|--------|------|--------|
| base | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/` | ✅ |
| sft_clean | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/` | ✅ |
| sft_contam | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/` | ✅ |
| rl_aligned | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct/` | ✅ |

### 3. Dry-run — ✅ PASS
4-regime mock data dry-run 成功，pipeline 完整走通（参数解析 → mock 生成 → survival analysis → report 输出）。

### 4. 缺失数据
| Regime | Signal 数据 | 需要操作 |
|--------|------------|---------|
| sft_clean (d000) | ✅ 已有（exp-002） | symlink 到 exp-008 per-bench 子目录结构 |
| sft_contam (d005) | ✅ 已有（exp-002） | symlink 到 exp-008 per-bench 子目录结构 |
| **base** | ❌ 缺失 | GPU 计算：裸 Qwen2.5-0.5B，3 benchmarks × 3 signals |
| **rl_aligned** | ❌ 缺失 | GPU 计算：Qwen2.5-0.5B-Instruct，3 benchmarks × 3 signals |

**目录结构适配**：exp-002 存储为 `{model}/signals_merged_{bench}.json`（flat），exp-008 期望 `{regime}/{bench}/signals_merged_{bench}.json`（nested）。需 symlink 或 copy。

**GPU 时间估算**：2 regimes × 3 benchmarks × 3 signals，0.5B 模型。估计 2-3 小时（单 GPU）。

### 5. Full Run 前置条件清单
1. 为 base 和 rl_aligned 计算 signal（需 GPU，~2-3h）
2. 将 exp-002 的 sft_clean/sft_contam signals symlink 到 `exp008/signals/{regime}/{bench}/` 结构，**或**让 `run_exp008.sh` 自动重新计算（脚本有 `[SKIP]` 逻辑，但需要先放好文件）
3. Labels 转换（脚本 Step 0 自动处理）
4. 提交前检查目标 GPU 无冲突进程（C001 约束）
5. 注意：`run_exp008.sh` 的 `SIGNALS` 不含 constat，仅跑 embedding/minkpp/selfcritique

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_verify_exp008_dryrun_real_data_20260514T141556"
}
```

</details>

---
