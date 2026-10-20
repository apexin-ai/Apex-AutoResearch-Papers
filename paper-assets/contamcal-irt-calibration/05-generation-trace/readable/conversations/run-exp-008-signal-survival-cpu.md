# run exp 008 signal survival cpu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_run_exp_008_signal_survival_cpu_20260514T160652.jsonl`
- **Structured JSON:** [`9619d7e181ab8ce1f0a7.json`](../../sessions/96/9619d7e181ab8ce1f0a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-14T16:09:48.499226+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T16:09:48.501776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T16:09:48.502077+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/exp008/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/exp008/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T16:09:48.502296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T16:09:48.502526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "/root/miniconda3/bin/python --version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "/root/miniconda3/bin/python --version"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T16:09:48.502754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nexp008_output\\nplot_survival.py\\nrun_exp008.sh\\nrun_exp008.sh.bak\\nrun_signal_survival.py\\nsignal_survival.py\\nsignal_survival_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T16:09:48.502973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen2.5-0.5B_d000_s42\\nQwen2.5-0.5B_d005_s42\\nQwen2.5-0.5B_d100_s42\\nbatch_report_Qwen2.5-0.5B.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T16:09:48.503180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Python 3.12.3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T16:09:48.516626+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration/exp008 && /root/miniconda3/bin/python run_signal_survival.py --help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration/exp008 && /root/miniconda3/bin/python run_signal_survival.py --help"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T16:09:48.517011+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T16:09:48.517240+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration/exp008 && /root/miniconda3/bin/python run_signal_survival.py --help",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration/exp008 && /root/miniconda3/bin/python run_signal_survival.py --help",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T16:09:48.517532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: run_signal_survival.py [-h] [--regime-dirs NAME=PATH [NAME=PATH ...]]\\n                              [--sft-signals-dir SFT_SIGNALS_DIR]\\n                              [--rl-signals-dir RL_SIGNALS_DIR]\\n                              [--labels-file LABELS_FILE]\\n                              [--output-dir OUTPUT_DIR] [--dry-run]\\n                              [--max-items MAX_ITEMS]\\n                              [--regime-names REGIME_NAMES [REGIME_NAMES ...]]\\n\\nexp-008: Signal Survival Analysis — N-regime comparison\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --regime-dirs NAME=PATH [NAME=PATH ...]\\n                        Regime directories as name=path pairs (order defines\\n                        adjacency)\\n  --sft-signals-dir SFT_SIGNALS_DIR\\n                        (Legacy) SFT signals directory\\n  --rl-signals-dir RL_SIGNALS_DIR\\n                        (Legacy) RL signals directory\\n  --labels-file LABELS_FILE\\n                        JSON file with contamination labels {index: 0/1}\\n  --output-dir OUTPUT_DIR\\n  --dry-run             Use synthetic mock data for validation\\n  --max-items MAX_ITEMS\\n                        Limit number of items (for dry-run or debugging)\\n  --regime-names REGIME_NAMES [REGIME_NAMES ...]\\n                        Regime names for dry-run (default: SFT RL)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T16:09:48.517830+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T16:09:48.518058+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"signal_embedding_arc_challenge.json\\nsignal_embedding_gsm8k.json\\nsignal_embedding_mmlu.json\\nsignal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json\\nsignal_minkpp_arc_challenge.json\\nsignal_minkpp_gsm8k.json\\nsignal_minkpp_mmlu.json\\nsignal_selfcritique_arc_challenge.json\\nsignal_selfcritique_gsm8k.json\\nsignal_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T16:09:48.518261+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T16:09:48.526285+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"signal_embedding_arc_challenge.json\\nsignal_embedding_gsm8k.json\\nsignal_embedding_mmlu.json\\nsignal_minkpp_arc_challenge.json\\nsignal_minkpp_gsm8k.json\\nsignal_minkpp_mmlu.json\\nsignal_selfcritique_arc_challenge.json\\nsignal_selfcritique_gsm8k.json\\nsignal_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T16:09:48.526621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T16:09:48.526842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -80 /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -80 /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T16:09:48.527064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"signal_embedding_arc_challenge.json\\nsignal_embedding_gsm8k.json\\nsignal_embedding_mmlu.json\\nsignal_minkpp_arc_challenge.json\\nsignal_minkpp_gsm8k.json\\nsignal_minkpp_mmlu.json\\nsignal_selfcritique_arc_challenge.json\\nsignal_selfcritique_gsm8k.json\\nsignal_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T16:09:48.533458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival — end-to-end execution script.\\nv2: Extended from SFT/RL pairwise to N-regime comparison.\\n\\nUsage:\\n  python run_signal_survival.py \\\\\\n    --regime-dirs base=/path/base SFT_clean=/path/sft RL=/path/rl \\\\\\n    --labels-file /path/to/labels.json \\\\\\n    --output-dir /path/to/exp008_output/\\n\\n  # Legacy 2-regime (still works):\\n  python run_signal_survival.py \\\\\\n    --sft-signals-dir /path/sft/ --rl-signals-dir /path/rl/ \\\\\\n    --labels-file labels.json\\n\\n  # Quick validation with mock data:\\n  python run_signal_survival.py --dry-run --max-items 10\\n  python run_signal_survival.py --dry-run --max-items 10 --regime-names base SFT RL DPO\\n\\nDependencies: numpy, scipy, sklearn\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nfrom signal_survival_analysis import (\\n    SIGNAL_KEYS,\\n    print_summary_table,\\n    run_survival_analysis,\\n    save_report,\\n)\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef load_signal_file(path: Path, signal_key: str) -> list[dict]:\\n    \\\"\\\"\\\"Load a signal JSON file and validate it has expected fields.\\\"\\\"\\\"\\n    with open(path) as f:\\n        data = json.load(f)\\n    if not isinstance(data, list) or len(data) == 0:\\n        raise ValueError(f\\\"Expected non-empty list in {path}\\\")\\n    if signal_key not in data[0]:\\n        raise ValueError(f\\\"Signal key '{signal_key}' not found in {path}\\\")\\n    return data\\n\\n\\ndef load_signals_from_dir(signals_dir: Path) -> dict[str, list[dict]]:\\n    \\\"\\\"\\\"\\n    Load all signal files from a directory.\\n    Returns {signal_key: [records]}.\\n    \\\"\\\"\\\"\\n    signals = {}\\n\\n    merged_files = list(signals_dir.glob(\\\"signals_merged_*.json\\\"))\\n    if merged_files:\\n        logger.info(\\\"Found
…[truncated 996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T16:09:48.533956+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/exp008 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/exp008 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T16:09:48.534197+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -200 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -200 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T16:09:48.534440+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp008/exp008_output/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/mmlu/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/gsm8k/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/arc_challenge/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_output/cliff_analysis.json\\n/root/contamcal-irt-calibration/exp008/exp008_output/cross_benchmark_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T16:09:48.534681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/exp008/exp008_output/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/exp008/exp008_output/"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T16:09:48.535099+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival Analysis — core analysis module.\\nv2: Extended from SFT/RL pairwise to N-regime comparison.\\n\\nComputes:\\n  - AUC matrix: N_signals x N_regimes AUROC for contamination detection\\n  - Pairwise tests: statistical tests between all adjacent regime pairs\\n    (Cohen's d, Spearman rho, AUROC ratio, Wilcoxon signed-rank)\\n\\nInput:  OrderedDict mapping regime_name -> {signal_key: [records]}, plus labels.\\nOutput: {regime_names, auc_matrix, pairwise_tests, per_signal (compat), summary}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom sklearn.metrics import roc_auc_score\\n\\nlogger = logging.getLogger(__name__)\\n\\nSIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\"]\\nSIGNAL_LABELS = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K%++\\\",\\n    \\\"s3_constat\\\": \\\"ConStat\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n}\\n\\n\\ndef cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:\\n    \\\"\\\"\\\"Cohen's d effect size between two groups.\\\"\\\"\\\"\\n    n1, n2 = len(group1), len(group2)\\n    if n1 < 2 or n2 < 2:\\n        return float(\\\"nan\\\")\\n    var1 = group1.var(ddof=1)\\n    var2 = group2.var(ddof=1)\\n    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))\\n    if pooled_std == 0:\\n        return float(\\\"nan\\\")\\n    return (group1.mean() - group2.mean()) / pooled_std\\n\\n\\ndef compute_single_regime_metrics(values: np.ndarray, labels: np.ndarray) -> dict:\\n    \\\"\\\"\\\"AUROC and Cohen's d for contamination detection in one regime.\\\"\\\"\\\"\\n    mask = ~(np.isnan(values) | np.isnan(labels))\\n    v = values[mask]\\n    lab = labels[mask].astype(int)\\n    contam = lab == 1\\n    clean = la
…[truncated 5149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T16:09:48.538625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cliff_analysis.json\\ncross_benchmark_summary.json\\nper_benchmark\\nsignal_decay_scatter.pdf\\nsurvival_auc_comparison.pdf\\nsurvival_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T16:09:48.538913+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -200 /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -200 /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T16:09:48.539410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\nimport numpy as np\\n\\nfrom signal_survival_analysis import (\\n    SIGNAL_KEYS,\\n    print_summary_table,\\n    run_survival_analysis,\\n    save_report,\\n)\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef load_signal_file(path: Path, signal_key: str) -> list[dict]:\\n    \\\"\\\"\\\"Load a signal JSON file and validate it has expected fields.\\\"\\\"\\\"\\n    with open(path) as f:\\n        data = json.load(f)\\n    if not isinstance(data, list) or len(data) == 0:\\n        raise ValueError(f\\\"Expected non-empty list in {path}\\\")\\n    if signal_key not in data[0]:\\n        raise ValueError(f\\\"Signal key '{signal_key}' not found in {path}\\\")\\n    return data\\n\\n\\ndef load_signals_from_dir(signals_dir: Path) -> dict[str, list[dict]]:\\n    \\\"\\\"\\\"\\n    Load all signal files from a directory.\\n    Returns {signal_key: [records]}.\\n    \\\"\\\"\\\"\\n    signals = {}\\n\\n    merged_files = list(signals_dir.glob(\\\"signals_merged_*.json\\\"))\\n    if merged_files:\\n        logger.info(\\\"Found merged signal file: %s\\\", merged_files[0])\\n        with open(merged_files[0]) as f:\\n            merged = json.load(f)\\n        for sig_key in SIGNAL_KEYS:\\n            if any(sig_key in r for r in merged):\\n                signals[sig_key] = merged\\n        return signals\\n\\n    key_to_filename_prefix = {\\n        \\\"s1_embedding\\\": \\\"signal_embedding_\\\",\\n        \\\"s2_minkpp\\\": \\\"signal_minkpp_\\\",\\n        \\\"s3_constat\\\": \\\"signal_constat_\\\",\\n        \\\"s4_selfcritique\\\": \\\"signal_selfcritique_\\\",\\n    }\\n    for sig_key, prefix in key_to_filename_prefix.items():\\n        matches = list(signals_dir.glob(f\\\"{prefix}*.json\\\"))\\n        if matches:\\n            signals[sig_key] = load_signal_file(matches[0], sig_key)\\n            logger.info(\\\"Loaded %s from %s (%d items)\\\", sig_key, matches[0], len(signals[sig_key]))\\n        
…[truncated 6317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T16:09:48.539687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"labels*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration -name \"labels*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T16:09:48.539897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T16:09:48.540116+00:00_

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
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
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

_source line 32 · 2026-05-14T16:09:48.546517+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -euo pipefail\\n\\nGPUS=\\\"${1:?Usage: bash run_exp008.sh GPU_IDS (e.g. 1,4,5)}\\\"\\n\\n# === Paths ===\\nBASE_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\"\\nINSTRUCT_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct\\\"\\nD000_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\\\"\\nD005_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\\\"  # d005: mixed 0/1 labels, AUC computable\\nSFT_DATA=\\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\\"\\nLABELS_DIR=\\\"/root/autodl-tmp/exp001/sft_data\\\"\\n\\nOUTPUT_BASE=\\\"/root/autodl-tmp/exp008\\\"\\nSIGNALS_DIR=\\\"${OUTPUT_BASE}/signals\\\"\\nRESULTS_DIR=\\\"${OUTPUT_BASE}/results\\\"\\n\\nBENCHMARKS=(mmlu gsm8k arc_challenge)\\nSIGNALS=\\\"embedding minkpp selfcritique\\\"\\n\\nSCRIPT_DIR=\\\"$(cd \\\"$(dirname \\\"$0\\\")\\\" && pwd)\\\"\\nCOMPUTE_SCRIPT=\\\"${SCRIPT_DIR}/../exp002/compute_signals.py\\\"\\nSURVIVAL_SCRIPT=\\\"${SCRIPT_DIR}/run_signal_survival.py\\\"\\n\\n# === Environment ===\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport CUDA_VISIBLE_DEVICES=\\\"$GPUS\\\"\\n\\n# === Regime definitions ===\\ndeclare -A REGIME_MODEL\\nREGIME_MODEL[base]=\\\"$BASE_MODEL\\\"\\nREGIME_MODEL[sft_clean]=\\\"$D000_ADAPTER\\\"\\nREGIME_MODEL[sft_contam]=\\\"$D005_ADAPTER\\\"\\nREGIME_MODEL[rl_aligned]=\\\"$INSTRUCT_MODEL\\\"\\nREGIMES=(base sft_clean sft_contam rl_aligned)\\n\\necho \\\"=== exp-008 Signal Survival ===\\\"\\necho \\\"GPUs: $GPUS | Benchmarks: ${BENCHMARKS[*]} | Signals: $SIGNALS\\\"\\necho \\\"Regimes: ${REGIMES[*]}\\\"\\necho \\\"\\\"\\n\\n# === Step 0: Convert labels to {index: 0/1} format ===\\nmkdir -p \\\"${OUTPUT_BASE}/labels\\\"\\nfor bench in \\\"${BENCHMARKS[@]}\\\"; do\\n    SRC=\\\"${LABELS_DIR}/contamination_labels_${bench}_d005.json\\\"\\n    DST=\\\"${OUTPUT_BASE}/labels/labels_${benc
…[truncated 2285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T16:09:48.546935+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/sft_data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/sft_data/"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T16:09:48.547202+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"contamination_labels_arc_challenge_d005.json\\ncontamination_labels_arc_challenge_d025.json\\ncontamination_labels_arc_challenge_d050.json\\ncontamination_labels_arc_challenge_d100.json\\ncontamination_labels_gsm8k_d005.json\\ncontamination_labels_gsm8k_d025.json\\ncontamination_labels_gsm8k_d050.json\\ncontamination_labels_gsm8k_d100.json\\ncontamination_labels_mmlu_d005.json\\ncontamination_labels_mmlu_d025.json\\ncontamination_labels_mmlu_d050.json\\ncontamination_labels_mmlu_d100.json\\ndata_meta.json\\ndata_meta_0pct.json\\nsft_dosage_000.jsonl\\nsft_dosage_005.jsonl\\nsft_dosage_025.jsonl\\nsft_dosage_050.jsonl\\nsft_dosage_100.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T16:09:48.547439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp008/labels/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp008/labels/"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T16:09:48.547638+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/exp008/labels/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T16:09:48.547827+00:00_

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
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
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

_source line 38 · 2026-05-14T16:09:48.548063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.3449670374393463,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T16:09:48.554353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -20 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -20 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T16:09:48.554737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"dosage\\\": 5,\\n  \\\"total_items\\\": 14042,\\n  \\\"contaminated_count\\\": 703,\\n  \\\"labels\\\": [\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T16:09:48.555034+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -20 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -20 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T16:09:48.555281+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"dosage\\\": 100,\\n  \\\"total_items\\\": 14042,\\n  \\\"contaminated_count\\\": 14042,\\n  \\\"labels\\\": [\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T16:09:48.555650+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat << 'PYEOF' > /root/contamcal-irt-calibration/exp008/run_exp002_survival.py\n\"\"\"\nRun exp-008 signal survival analysis using exp-002 signal data.\nCreates per-benchmark symlinked directories, converts labels, runs analysis.\n\"\"\"\nimport json\nimport os\nimport sys\nfrom pathlib import Path\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nREGIMES = [(\"d000\", \"Qwen2.5-0.5B_d000_s42\"),\n           (\"d005\", \"Qwen2.5-0.5B_d005_s42\"),\n           (\"d100\", \"Qwen2.5-0.5B_d100_s42\")]\n\nEXP002_SIGNALS = Path(\"/root/autodl-tmp/exp002/signals\")\nLABELS_SRC = Path(\"/root/autodl-tmp/exp001/sft_data\")\nWORK_DIR = Path(\"/root/autodl-tmp/exp008_from_exp002\")\nOUTPUT_DIR = Path(\"/root/contamcal-irt-calibration/exp008/exp008_exp002_output\")\n\ndef convert_labels(bench):\n    \"\"\"Convert array-format labels to {index: 0/1} dict format.\"\"\"\n    src = LABELS_SRC / f\"contamination_labels_{bench}_d005.json\"\n    dst = WORK_DIR / \"labels\" / f\"labels_{bench}.json\"\n    dst.parent.mkdir(parents=True, exist_ok=True)\n    with open(src) as f:\n        raw = json.load(f)\n    labels = {str(i): v for i, v in enumerate(raw[\"labels\"])}\n    with open(dst, \"w\") as f:\n        json.dump(labels, f)\n    print(f\"Labels {bench}: {raw['contaminated_count']}/{raw['total_items']} contaminated -> {dst}\")\n    return dst\n\ndef setup_signal_dirs(bench):\n    \"\"\"Create per-regime directories with symlinks to the right benchmark signal files.\"\"\"\n    regime_args = []\n    for regime_name, dir_name in REGIMES:\n        src_dir = EXP002_SIGNALS / dir_name\n        dst_dir = WORK_DIR / \"signals\" / regime_name / bench\n        dst_dir.mkdir(parents=True, exist_ok=True)\n        \n        merged_src = src_dir / f\"signals_merged_{bench}.json\"\n        merged_dst = dst_dir / f\"signals_merged_{bench}.json\"\n        if merged_src.exists():\n            if merged_dst.exists() or merged_dst.is_symlink():\n                merged_dst.unlink()\n            os.symlink(merged_src, merged_dst)\n        \n        for sig_prefix in [\"signal_embedding_\", \"signal_minkpp_\", \"signal_selfcritique_\"]:\n            sig_src = src_dir / f\"{sig_prefix}{bench}.json\"\n            sig_dst = dst_dir / f\"{sig_prefix}{bench}.json\"\n            if sig_src.exists():\n                if sig_dst.exists() or sig_dst.is_symlink():\n                    sig_dst.unlink()\n                os.symlink(sig_src, sig_dst)\n        \n        regime_args.append(f\"{regime_name}={dst_dir}\")\n    return regime_args\n\ndef main():\n    WORK_DIR.mkdir(parents=True, exist_ok=True)\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    \n    script_dir = Path(__file__).parent\n    survival_script = script_dir / \"run_signal_survival.py\"\n    \n    all_results = {}\n    \n    for bench in BENCHMARKS:\n        print(f\"\\n{'='*60}\")\n        print(f\"Benchmark: {bench}\")\n        print(f\"{'='*60}\")\n        \n        labels_file = convert_labels(bench)\n        regime_args = setup_signal_dirs(bench)\n        \n        out_dir = OUTPUT_DIR / \"per_benchmark\" / bench\n        out_dir.mkdir(parents=True, exist_ok=True)\n        \n        cmd = [\n            sys.executable,\n            str(survival_script),\n            \"--regime-dirs\"] + regime_args + [\n            \"--labels-file\", str(labels_file),\n            \"--output-dir\", str(out_dir),\n        ]\n        \n        print(f\"CMD: {' '.join(cmd)}\")\n        ret = os.system(\" \".join(cmd))\n        \n        report_file = out_dir / \"survival_report.json\"\n        if report_file.exists():\n            with open(report_file) as f:\n                report = json.load(f)\n            all_results[bench] = report\n            print(f\"[OK] {bench} -> {report_file}\")\n        else:\n            print(f\"[FAIL] {bench} - no report generated (exit code {ret})\")\n    \n    # Cross-benchmark summary\n    if all_results:\n        summary_file = OUTPUT_DIR / \"cross_benchmark_summary.json\"\n        with open(summary_file, \"w\") as f:\n            json.dump(all_results, f, indent=2, default=str)\n        print(f\"\\n{'='*60}\")\n        print(f\"Cross-benchmark summary -> {summary_file}\")\n        \n        # Print AUC heatmap\n        print(f\"\\n{'='*60}\")\n        print(\"AUC HEATMAP (signal × regime, per benchmark)\")\n        print(f\"{'='*60}\")\n        for bench, report in all_results.items():\n            print(f\"\\n--- {bench} ---\")\n            auc_matrix = report.get(\"auc_matrix\", {})\n            if auc_matrix:\n                regimes = report.get(\"regime_names\", [])\n                signals = list(auc_matrix.keys())\n                header = f\"{'Signal':<20}\" + \"\".join(f\"{r:>12}\" for r in regimes)\n                print(header)\n                for sig in signals:\n                    vals = auc_matrix[sig]\n                    row = f\"{sig:<20}\"\n                    for r in regimes:\n                        v = vals.get(r)\n                        row += f\"{v:>12.4f}\" if v is not None else f\"{'N/A':>12}\"\n                    print(row)\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat << 'PYEOF' > /root/contamcal-irt-calibration/exp008/run_exp002_survival.py\n\"\"\"\nRun exp-008 signal survival analysis using exp-002 signal data.\nCreates per-benchmark symlinked directories, converts labels, runs analysis.\n\"\"\"\nimport json\nimport os\nimport sys\nfrom pathlib import Path\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nREGIMES = [(\"d000\", \"Qwen2.5-0.5B_d000_s42\"),\n           (\"d005\", \"Qwen2.5-0.5B_d005_s42\"),\n           (\"d100\", \"Qwen2.5-0.5B_d100_s42\")]\n\nEXP002_SIGNALS = Path(\"/root/autodl-tmp/exp002/signals\")\nLABELS_SRC = Path(\"/root/autodl-tmp/exp001/sft_data\")\nWORK_DIR = Path(\"/root/autodl-tmp/exp008_from_exp002\")\nOUTPUT_DIR = Path(\"/root/contamcal-irt-calibration/exp008/exp008_exp002_output\")\n\ndef convert_labels(bench):\n    \"\"\"Convert array-format labels to {index: 0/1} dict format.\"\"\"\n    src = LABELS_SRC / f\"contamination_labels_{bench}_d005.json\"\n    dst = WORK_DIR / \"labels\" / f\"labels_{bench}.json\"\n    dst.parent.mkdir(parents=True, exist_ok=True)\n    with open(src) as f:\n        raw = json.load(f)\n    labels = {str(i): v for i, v in enumerate(raw[\"labels\"])}\n    with open(dst, \"w\") as f:\n        json.dump(labels, f)\n    print(f\"Labels {bench}: {raw['contaminated_count']}/{raw['total_items']} contaminated -> {dst}\")\n    return dst\n\ndef setup_signal_dirs(bench):\n    \"\"\"Create per-regime directories with symlinks to the right benchmark signal files.\"\"\"\n    regime_args = []\n    for regime_name, dir_name in REGIMES:\n        src_dir = EXP002_SIGNALS / dir_name\n        dst_dir = WORK_DIR / \"signals\" / regime_name / bench\n        dst_dir.mkdir(parents=True, exist_ok=True)\n        \n        merged_src = src_dir / f\"signals_merged_{bench}.json\"\n        merged_dst = dst_dir / f\"signals_merged_{bench}.json\"\n        if merged_src.exists():\n            if merged_dst.exists() or merged_dst.is_symlink():\n                merged_dst.unlink()\n            os.symlink(merged_src, merged_dst)\n        \n        for sig_prefix in [\"signal_embedding_\", \"signal_minkpp_\", \"signal_selfcritique_\"]:\n            sig_src = src_dir / f\"{sig_prefix}{bench}.json\"\n            sig_dst = dst_dir / f\"{sig_prefix}{bench}.json\"\n            if sig_src.exists():\n                if sig_dst.exists() or sig_dst.is_symlink():\n                    sig_dst.unlink()\n                os.symlink(sig_src, sig_dst)\n        \n        regime_args.append(f\"{regime_name}={dst_dir}\")\n    return regime_args\n\ndef main():\n    WORK_DIR.mkdir(parents=True, exist_ok=True)\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    \n    script_dir = Path(__file__).parent\n    survival_script = script_dir / \"run_signal_survival.py\"\n    \n    all_results = {}\n    \n    for bench in BENCHMARKS:\n        print(f\"\\n{'='*60}\")\n        print(f\"Benchmark: {bench}\")\n        print(f\"{'='*60}\")\n        \n        labels_file = convert_labels(bench)\n        regime_args = setup_signal_dirs(bench)\n        \n        out_dir = OUTPUT_DIR / \"per_benchmark\" / bench\n        out_dir.mkdir(parents=True, exist_ok=True)\n        \n        cmd = [\n            sys.executable,\n            str(survival_script),\n            \"--regime-dirs\"] + regime_args + [\n            \"--labels-file\", str(labels_file),\n            \"--output-dir\", str(out_dir),\n        ]\n        \n        print(f\"CMD: {' '.join(cmd)}\")\n        ret = os.system(\" \".join(cmd))\n        \n        report_file = out_dir / \"survival_report.json\"\n        if report_file.exists():\n            with open(report_file) as f:\n                report = json.load(f)\n            all_results[bench] = report\n            print(f\"[OK] {bench} -> {report_file}\")\n        else:\n            print(f\"[FAIL] {bench} - no report generated (exit code {ret})\")\n    \n    # Cross-benchmark summary\n    if all_results:\n        summary_file = OUTPUT_DIR / \"cross_benchmark_summary.json\"\n        with open(summary_file, \"w\") as f:\n            json.dump(all_results, f, indent=2, default=str)\n        print(f\"\\n{'='*60}\")\n        print(f\"Cross-benchmark summary -> {summary_file}\")\n        \n        # Print AUC heatmap\n        print(f\"\\n{'='*60}\")\n        print(\"AUC HEATMAP (signal × regime, per benchmark)\")\n        print(f\"{'='*60}\")\n        for bench, report in all_results.items():\n            print(f\"\\n--- {bench} ---\")\n            auc_matrix = report.get(\"auc_matrix\", {})\n            if auc_matrix:\n                regimes = report.get(\"regime_names\", [])\n                signals = list(auc_matrix.keys())\n                header = f\"{'Signal':<20}\" + \"\".join(f\"{r:>12}\" for r in regimes)\n                print(header)\n                for sig in signals:\n                    vals = auc_matrix[sig]\n                    row = f\"{sig:<20}\"\n                    for r in regimes:\n                        v = vals.get(r)\n                        row += f\"{v:>12.4f}\" if v is not None else f\"{'N/A':>12}\"\n                    print(row)\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T16:09:48.555983+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T16:09:48.556220+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration/exp008 && /root/miniconda3/bin/python run_exp002_survival.py 2>&1",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration/exp008 && /root/miniconda3/bin/python run_exp002_survival.py 2>&1",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T16:09:48.562694+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 00:09:28,423 [INFO] Loading signals for regime 'd000' from /root/autodl-tmp/exp008_from_exp002/signals/d000/mmlu\\n2026-05-15 00:09:28,423 [INFO] Found merged signal file: /root/autodl-tmp/exp008_from_exp002/signals/d000/mmlu/signals_merged_mmlu.json\\n2026-05-15 00:09:28,463 [INFO] Loading signals for regime 'd005' from /root/autodl-tmp/exp008_from_exp002/signals/d005/mmlu\\n2026-05-15 00:09:28,464 [INFO] Found merged signal file: /root/autodl-tmp/exp008_from_exp002/signals/d005/mmlu/signals_merged_mmlu.json\\n2026-05-15 00:09:28,502 [INFO] Loading signals for regime 'd100' from /root/autodl-tmp/exp008_from_exp002/signals/d100/mmlu\\n2026-05-15 00:09:28,503 [INFO] Found merged signal file: /root/autodl-tmp/exp008_from_exp002/signals/d100/mmlu/signals_merged_mmlu.json\\n2026-05-15 00:09:28,550 [INFO] Running survival analysis...\\n2026-05-15 00:09:28,615 [INFO] Embedding: AUC d000=0.5049 -> d005=0.953 -> d100=0.4943\\n2026-05-15 00:09:28,679 [INFO] Min-K%++: AUC d000=0.509 -> d005=0.4655 -> d100=0.5053\\n2026-05-15 00:09:28,700 [INFO] ConStat: AUC d000=None -> d005=None -> d100=None\\n2026-05-15 00:09:28,755 [INFO] Self-Critique: AUC d000=0.4957 -> d005=0.5165 -> d100=0.5125\\n2026-05-15 00:09:28,756 [INFO] Report saved to /root/contamcal-irt-calibration/exp008/exp008_exp002_output/per_benchmark/mmlu/survival_report.json\\n2026-05-15 00:09:28,756 [INFO] Done. Output in /root/contamcal-irt-calibration/exp008/exp008_exp002_output/per_benchmark/mmlu\\n\\n=================================================\\nSignal Survival Analysis -- 3 regimes: d000 -> d005 -> d100\\n=================================================\\nSignal                 d000       d005       d100\\n-------------------------------------------------\\nEmbedding            0.5049     0.9530     0.4943\\nMin-K%++             0.5090     0.4655     0.5053\\nConStat                 N/A        N/A        N/A\\nSelf-Critique        0.4957    
…[truncated 6417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T16:09:48.562973+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/exp008/exp008_exp002_output -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/exp008/exp008_exp002_output -type f"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T16:09:48.563165+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp008/exp008_exp002_output/per_benchmark/mmlu/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_exp002_output/per_benchmark/gsm8k/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_exp002_output/per_benchmark/arc_challenge/survival_report.json\\n/root/contamcal-irt-calibration/exp008/exp008_exp002_output/cross_benchmark_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-14T16:09:48.563446+00:00_

运行成功。结果汇总：

## 产出文件
- `exp008_exp002_output/cross_benchmark_summary.json` — 跨 benchmark 汇总
- `exp008_exp002_output/per_benchmark/{mmlu,gsm8k,arc_challenge}/survival_report.json` — 各 benchmark 详细报告

## AUC Heatmap（3 signals × 3 regimes × 3 benchmarks）

ConStat (S3) 在 exp-002 中未计算，全部 N/A。

| Signal | Regime | mmlu | gsm8k | arc_challenge |
|---|---|---|---|---|
| **Embedding (S1)** | d000 | 0.5049 | 0.5502 | 0.4270 |
| | d005 | **0.9530** | **0.9882** | **0.9950** |
| | d100 | 0.4943 | 0.4127 | 0.5010 |
| **Min-K%++ (S2)** | d000 | 0.5090 | 0.5697 | 0.5075 |
| | d005 | 0.4655 | 0.4649 | 0.4659 |
| | d100 | 0.5053 | 0.4841 | 0.4950 |
| **Self-Critique (S4)** | d000 | 0.4957 | 0.4800 | 0.5175 |
| | d005 | 0.5165 | 0.4947 | 0.4325 |
| | d100 | 0.5125 | 0.4393 | 0.5515 |

关键发现：
- **Embedding (S1) 在 d005 regime 下 AUC 极高**（0.95-0.995），但在 d000 和 d100 下降至随机水平（~0.5）。信号未能 survive 到 d100 regime。
- **Min-K%++ 和 Self-Critique 在所有 regime 下都接近随机**（0.43-0.57），无有效区分能力。
- **Surviving signals: 0/4**（所有 benchmark 一致）— 没有信号在跨 regime 下保持检测能力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_run_exp_008_signal_survival_cpu_20260514T160652"
}
```

</details>

---
